# Quality Root-Cause Agent Data Dictionary

This demo uses three CSV files and two past investigation reports. All records are fictitious training data.

The two weekly CSVs come from the Copilot scenario's workbook and keep its columns; see that scenario's [data dictionary](<../../Copilot/Manufacturing Operations Performance & Risk/DATA_DICTIONARY.md>) for every column. The shift CSV and both reports are new. A copy of the original workbook sits in `data/` for reference; the demo does not read it.

## Plain-language glossary

The reports use the plain-language labels below. Technical terms and CSV field names are unchanged, so you can match them to the data and code.

| Plain-language label | Technical term / field | Meaning in this demo |
|---|---|---|
| First-inspection pass rate | First-pass yield (FPY); `First Pass Yield Actual`, `fpy` | Share of inspected products that pass the first time, before rework or retesting |
| Soldering oven temperature | Reflow Zone 3 temperature; `reflow_zone3_temp_c` | Temperature in one section of the oven used to join electronic parts with soldering material |
| Soldering material batch | Solder-paste lot; `solder_paste_lot` | A production batch of metal-based paste used to make soldered connections, not an adhesive |
| Oven heating conditions | Reflow profile | Temperature and time conditions during soldering, not just a single temperature reading |
| Incoming material quality check | Incoming inspection; `incoming_inspection_result` | Quality check on a material batch before production use |
| Near the acceptance limit | `marginal` | A synthetic inspection result close to the acceptance limit that requires further checking; not proof that the material caused the decline |
| Past investigation report | Root-cause analysis (RCA) report | A previous incident's evidence, findings, actions, and lessons |
| Reporting week / work period | `week`, `shift` | W40 means week 40; Day and Night are the two work periods within each date |

## operations_data.csv

Weekly operating data from the Copilot workbook's `Operations_Data` sheet: one row per week, plant, line, and product family. The 18 columns and their values are unchanged. The file has 16 rows; the workbook had 17, and one duplicate W43 Sensor Pack row was removed. The names `Plant-A` and `Drivetrain` are written as `Plant A` and `Drive Train`.

The demo reads these columns for Plant A Line 1 (Power Module):

| Column | Unit | Meaning |
|---|---|---|
| Completed Units | Units | Good units finished during the week; throughput, not the shift inspection sample |
| Scrap Units | Units | Units discarded rather than reworked; not the same as first-inspection failures |
| Downtime Minutes | Minutes | Time the line was stopped |
| OEE | Ratio, 0-1 | Overall equipment effectiveness, a composite score copied as supplied |

`Week`, `Plant`, `Line`, and `Product Family` identify each row. Values are copied as supplied, not recalculated. The `Quality` column in this file is not the first-inspection pass rate; use `First Pass Yield Actual` from the next file.

## quality_supplier_risk.csv

Weekly quality and supplier data from the Copilot workbook's `Quality_and_Supplier_Risk` sheet: one row per week, plant, line, and product family. It has 16 rows and 17 columns, unchanged apart from the same name changes as above.

`First Pass Yield Actual` is the weekly first-inspection pass rate that the shift records must match. For Plant A Line 1 (Power Module) it is W40: 0.975, W41: 0.969, W42: 0.936, and W43: 0.977.

The demo reads these columns:

| Column | Unit | Meaning |
|---|---|---|
| First Pass Yield Actual | Ratio, 0-1 | Share of products passing the first inspection without rework; the reference for the shift records |
| Supplier | Text | Key supplier of the line in the original sample: Supplier Nova |
| Material Group | Text | What that supplier provides: PCB (printed circuit board), not soldering paste |

Nova is the line's PCB supplier. The data names no supplier for the soldering paste and holds no incoming-inspection result for it. The other columns are described in the Copilot data dictionary. Two to note: `First Pass Yield Target` is 0.98 in this sample, and `Scrap Rate` is not `1 - FPY`, because failed units may be reworked.

## process_parameters.csv

New synthetic shift-level records for **Plant A Line 1 (Power Module)**. Coverage is W40-W43, seven days per week, with Day and Night shifts: **56 records and 13 columns**. One row represents one date and shift on the target line.

The soldering material batch is an added process-material setting with no named supplier. `incoming_inspection_result` is added synthetic batch evidence, not a field copied from the original weekly data.

| Column | Type | Unit / format | Meaning | Key / relationship |
|---|---|---|---|---|
| week | Text | W40-W43 | Week label matching the weekly data | Joins to `Week` |
| date | Date | YYYY-MM-DD | Synthetic shift-start date using the 2026 ISO calendar | Part of the shift identifier |
| shift | Text | Day / Night | Work period assigned to its start date | Part of the shift identifier; not a duration |
| plant | Text | Plant A | Plant identifier | Joins to `Plant` |
| line | Text | Line 1 | Line identifier | Joins to `Line` |
| product_family | Text | Power Module | Product family | Joins to `Product Family` |
| reflow_zone3_temp_c | Number | Degrees Celsius | Synthetic shift-average oven-sensor temperature in Zone 3 | Not a component's complete temperature and time curve |
| solder_paste_lot | Text | Synthetic batch identifier | Soldering material batch used during the shift | Groups shifts for material-batch comparisons |
| operator_id | Text | Synthetic operator identifier | Operator associated with the shift | Groups shifts for operator comparisons |
| units_tested | Integer | Units | Number of products receiving their first inspection during the shift | Positive denominator for the pass rate |
| units_failed | Integer | Units | Units failing the first inspection | Between zero and `units_tested` |
| fpy | Number | Ratio, 0-1 | First-inspection pass rate: `1 - units_failed / units_tested` | Recomputed from inspection counts |
| incoming_inspection_result | Text | accepted / marginal | Synthetic incoming material quality-check result for the soldering material batch | Repeated batch-level evidence, not a new inspection on each shift |

Join the weekly data on week, plant, line, and product family. Calculate the weekly first-inspection pass rate as `1 - sum(units_failed) / sum(units_tested)`, not the simple mean of shift pass rates. Each week's result must be within 0.005 (0.5 percentage points) of the original weekly pass rate.

`fpy` is rounded to ten decimal places; the stored value differs from its count-based calculation by at most 0.00000000005. Aggregate the integer counts rather than averaging rounded rates.

### Synthetic settings and interpretation

- **Calendar:** W40 is 2026-09-28 to 2026-10-04; W41 is 2026-10-05 to 2026-10-11; W42 is 2026-10-12 to 2026-10-18; W43 is 2026-10-19 to 2026-10-25. This year and date mapping are added demo conventions, not dates recovered from the original workbook.
- **Temperature:** The fictional reference is 245 +/- 5 degrees Celsius, giving a 240-250 range. These are teaching values, not recommended manufacturing settings. W41 shows a late upward trend, 12 W42 shifts exceed 250, and all W43 shifts return within the range.
- **Material:** SP-001 is used in W40-W41 with an `accepted` inspection label. SP-002 starts on the first W42 shift with a `marginal` label and remains in use throughout W43. Neither batch is assigned to Nova or another supplier.
- **Inspection labels:** `accepted` means the fictional incoming check was satisfactory; `marginal` means near the acceptance limit and requiring further checking. No actual test measurement, acceptance threshold, or material-release decision is recorded.
- **Operators:** OP-01 to OP-03 are present before W42. OP-04 first appears on 2026-10-14 and remains present during W43 recovery. All identifiers are fictitious.
- **Counts:** Each week has a synthetic inspection sample of 1,000 units, distributed across shifts of 65, 70, or 75 units. This is not a production census and is not assumed to equal `Completed Units`. First-inspection failures are not equivalent to scrapped units.

### Validation results

These are the results of the checks run on the data. Displayed rates are rounded; the weekly CSV values are unchanged.

| Week | Tested | Failed | Calculated FPY | Original weekly FPY | Difference, percentage points |
|---|---|---|---|---|---|
| W40 | 1000 | 25 | 97.5000% | 97.5000% | 0.0000 |
| W41 | 1000 | 31 | 96.9000% | 96.9000% | 0.0000 |
| W42 | 1000 | 64 | 93.6000% | 93.6000% | 0.0000 |
| W43 | 1000 | 23 | 97.7000% | 97.7000% | 0.0000 |

- All 56 rows have valid count-derived rates, unique shift keys, matching week/date labels, and weekly joins. Every date has one Day and one Night row.
- Temperature and FPY have Pearson correlations of **-0.9076 overall** and **-0.9385 within W42**. The association was built into the teaching data on purpose, so it is not evidence of a real-world cause.
- W42 shifts above the fictional temperature limit have **92.7907% FPY**, versus **98.5714%** for the two within-range shifts.
- For the operator check only, a high-defect shift means FPY below 95%; this is not a risk rule from the original workbook. W42 has ten such shifts, none assigned to OP-04. OP-04's two W42 shifts have 140 inspections, two failures, and **98.5714% FPY**.
- SP-002 remains in use during W43 recovery. A before/after batch comparison alone cannot isolate a material effect because the process conditions also changed.

### Evidence boundaries

The synthetic data supports comparing hypotheses, not confirming a root cause. Operator assignments and temperatures are not balanced experimental groups. OP-04's lack of overlap with poor results does not prove operator capability or establish that operator changes have no effect.

Current defect types, sensor-calibration records, a full heating curve, and controlled material trials are absent. A historical report cannot supply those missing facts for W42. The Quality Engineer must decide which additional measurements and controlled checks are needed.

## Knowledge documents

Two synthetic past investigation reports are available for local reading. Cite the document filename and relevant section when using a precedent; a past root-cause finding does not prove the cause of the current incident.

| Document | Document type | Scope / version | Evidence role | Provenance |
|---|---|---|---|---|
| [rca_2025_reflow_profile_drift.md](knowledge/rca_2025_reflow_profile_drift.md) | Past investigation report | Fictional 2025 incident, Plant A Line 1 / Power Module | Similar oven/material mechanism to assess, not proof of the current cause | Newly created Contoso training material |
| [rca_2024_connector_misalignment.md](knowledge/rca_2024_connector_misalignment.md) | Past investigation report | Fictional 2024 incident, Plant B Line 2 / Sensor Pack | Different line and mechanical mechanism; not support for a current oven cause | Newly created Contoso training material |

Both reports use the same six sections: Summary, Symptom, Investigation, Root cause, Corrective action, and Lessons. Each is a short, one-page record that uses the glossary labels.
