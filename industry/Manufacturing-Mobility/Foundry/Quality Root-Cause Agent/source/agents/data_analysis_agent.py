import json
from pathlib import Path

import pandas as pd
from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient

BASE = Path(__file__).resolve().parents[2]
WEEKS = ["W40", "W41", "W42", "W43"]
TEMP, BATCH, OPERATOR = "reflow_zone3_temp_c", "solder_paste_lot", "operator_id"
COUNTS = ["units_tested", "units_failed"]


def _rates(frame: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    totals = frame.groupby(keys).agg(
        shifts=("units_tested", "size"), units_tested=("units_tested", "sum"),
        units_failed=("units_failed", "sum"),
    )
    totals["pass_rate_pct"] = (100 * (1 - totals.units_failed / totals.units_tested)).round(4)
    return totals.reset_index()


@tool
def analyze_data() -> str:
    """Calculate Contoso Plant A Line 1 evidence from the three supplied CSV files."""
    weekly = []
    for name in ("operations_data.csv", "quality_supplier_risk.csv"):
        frame = pd.read_csv(BASE / "data" / name)
        selected = frame.loc[
            frame["Plant"].eq("Plant A") & frame["Line"].eq("Line 1")
            & frame["Product Family"].eq("Power Module")
        ].set_index("Week").sort_index()
        if selected.index.tolist() != WEEKS or selected.isna().any().any():
            raise ValueError(f"{name}: require one complete Plant A Line 1 record per W40-W43.")
        weekly.append(selected)
    operations, quality = weekly
    p = pd.read_csv(BASE / "data" / "process_parameters.csv").sort_values(["date", "shift"])
    if p.shape != (56, 13) or p.isna().any().any() or p.duplicated(["date", "shift"]).any():
        raise ValueError("process_parameters.csv: require 56 complete, unique shift records with 13 columns.")
    dates = pd.to_datetime(p["date"], format="%Y-%m-%d", errors="raise")
    valid_scope = p.plant.eq("Plant A") & p.line.eq("Line 1") & p.product_family.eq("Power Module")
    if not (valid_scope.all() and p["shift"].isin(["Day", "Night"]).all()
            and dates.dt.year.eq(2026).all() and ("W" + dates.dt.isocalendar().week.astype(str)).eq(p.week).all()
            and p.week.value_counts().reindex(WEEKS, fill_value=0).eq(14).all()):
        raise ValueError("process_parameters.csv: unexpected plant, line, product, shift, date, or week.")
    counts = p[COUNTS]
    if not (counts.mod(1).eq(0).all().all() and p.units_tested.gt(0).all()
            and p.units_failed.between(0, p.units_tested).all()):
        raise ValueError("process_parameters.csv: inspection counts must be valid integers.")
    calculated = 1 - p.units_failed / p.units_tested
    if (p.fpy - calculated).abs().gt(5.1e-11).any():
        raise ValueError("process_parameters.csv: stored pass rates disagree with inspection counts.")
    p["fpy"] = calculated
    totals = p.groupby("week")[COUNTS].sum()
    weighted = 1 - totals.units_failed / totals.units_tested
    if (weighted - quality["First Pass Yield Actual"]).abs().gt(0.005).any():
        raise ValueError("process_parameters.csv: weekly pass rates differ from the quality reference by >0.5 pp.")
    p["above_250_c"] = p[TEMP].gt(250)
    w42 = p.loc[p.week.eq("W42")]
    evidence = {
        "scope": "Contoso Plant A Line 1 / Power Module; synthetic training evidence",
        "sources": ["data/operations_data.csv", "data/quality_supplier_risk.csv", f"data/process_parameters.csv (temperature: {TEMP}; first-seen: date)"],
        "weekly_quality": quality[["First Pass Yield Actual", "Supplier", "Material Group"]].reset_index().to_dict("records"),
        "weekly_operations": operations[["Completed Units", "Scrap Units", "Downtime Minutes", "OEE"]].reset_index().to_dict("records"),
        "weekly_inspections": _rates(p, ["week"]).to_dict("records"),
        "temperature_ranges_c": p.groupby("week")[TEMP].agg(["min", "max"]).reset_index().to_dict("records"),
        "w41_last_eight_temperatures_c": p.loc[p.week.eq("W41"), TEMP].tail(8).tolist(),
        "temperature_pass_rate_correlation": round(p[TEMP].corr(p.fpy), 4),
        "w42_temperature_pass_rate_correlation": round(w42[TEMP].corr(w42.fpy), 4),
        "temperature_groups": _rates(p, ["week", "above_250_c"]).to_dict("records"),
        "material_groups": _rates(p, ["week", BATCH, "incoming_inspection_result"]).to_dict("records"),
        "operator_groups": _rates(p, ["week", OPERATOR]).to_dict("records"),
        "operator_first_seen": p.groupby(OPERATOR)["date"].min().to_dict(),
        "w42_below_95_pct_by_operator": w42.assign(below_95=w42.fpy.lt(0.95)).groupby(OPERATOR).below_95.sum().to_dict(),
    }
    return json.dumps(evidence, allow_nan=False)


def create_data_agent(client: FoundryChatClient) -> Agent:
    return Agent(client, name="DataAnalysisAgent", tools=[analyze_data],
                 default_options={"tool_choice": "required"}, instructions=(
        "Call analyze_data once before answering. Use only its evidence for Plant A Line 1 / Power Module. "
        "Summarize W40-W43 first-inspection pass rates, W41 temperature drift, W42 temperature groups, "
        "material batches and operators, including W43 recovery. Cite CSV filename and columns for each finding. "
        "Use count-weighted rates, not an average of shift rates. Preserve counts and important comparisons. "
        "The 240-250 C range and <95% high-defect flag are fictional teaching references, not production limits. "
        "Supplier Nova supplies PCB; no soldering material supplier is identified. Repeated incoming-check labels "
        "describe one batch, not independent tests. Shift samples are not production totals. "
        "Use plain English; associations do not prove causes. If evidence is unavailable, state that explicitly."
    ))
