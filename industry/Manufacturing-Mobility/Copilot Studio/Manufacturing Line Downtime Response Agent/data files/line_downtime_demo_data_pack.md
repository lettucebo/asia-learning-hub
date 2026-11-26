# Line Downtime Demo Data Pack (fictional, for training only)

This document contains all structured demo data for the Line Downtime Response Agent. Each section is one source table.


## incoming_quality_rejections

| reject_id | date | supplier | material_code | reason | rejected_qty |
|---|---|---|---|---|---|
| RJ-1182 | 2026-10-17 | Orion Metals | MAT-SHT-442 | Thickness variance | 240 |
| RJ-1199 | 2026-10-21 | Shakti Components | MAT-BRG-220 | Bearing noise above spec | 180 |

## machine_alarms

| timestamp | line_id | machine_id | alarm_code | severity | duration_min |
|---|---|---|---|---|---|
| 2026-10-18T02:14:00 | P-204 | FM-12 | ALM-HT-09 | High | 37 |
| 2026-10-18T05:41:00 | P-204 | CV-03 | ALM-MTR-02 | Medium | 19 |
| 2026-10-19T21:08:00 | P-204 | FM-12 | ALM-HT-09 | High | 22 |
| 2026-10-20T00:33:00 | P-204 | PK-07 | ALM-SNS-04 | Low | 11 |
| 2026-10-21T03:52:00 | P-204 | FM-12 | ALM-HT-09 | High | 29 |

## maintenance_tickets

| ticket_id | created_at | line_id | machine_id | issue | priority | status | owner |
|---|---|---|---|---|---|---|---|
| MT-14021 | 2026-10-18T02:26:00 | P-204 | FM-12 | Overheat and emergency stop | High | Open | Ravi Kumar |
| MT-14037 | 2026-10-19T21:22:00 | P-204 | FM-12 | Coolant flow instability | High | In Progress | Aditi Sharma |
| MT-14074 | 2026-10-21T04:05:00 | P-204 | CV-03 | Motor vibration above threshold | Medium | Open | Sameer Rao |

## material_criticality_matrix

| material_code | description | criticality | primary_line | alternate_supplier |
|---|---|---|---|---|
| MAT-BRG-220 | Bearing Assembly | High | Line A | No |
| MAT-SEAL-118 | Seal Ring | Medium | Line B | Yes |
| MAT-SHT-442 | Sheet Metal Panel | High | Line A | Limited |

## open_purchase_orders

| po_id | supplier | material_code | qty | expected_date | status | line_impact |
|---|---|---|---|---|---|---|
| PO-88214 | Shakti Components | MAT-BRG-220 | 5000 | 2026-10-24 | Delayed | High |
| PO-88277 | Delta Polymers | MAT-SEAL-118 | 12000 | 2026-10-27 | In Transit | Medium |
| PO-88310 | Orion Metals | MAT-SHT-442 | 3000 | 2026-10-26 | Delayed | High |

## quality_defects_weekly

| week_start | line_id | units_produced | defect_rate_pct | scrap_kg |
|---|---|---|---|---|
| 2026-10-12 | P-204 | 142500 | 1.6 | 890 |
| 2026-10-19 | P-204 | 137800 | 2.1 | 1140 |

## spare_parts_inventory

| part_no | description | on_hand | reorder_level | lead_time_days | primary_machine |
|---|---|---|---|---|---|
| SP-HTR-221 | Heater Coil Module | 3 | 8 | 12 | FM-12 |
| SP-MTR-903 | Conveyor Motor | 6 | 6 | 9 | CV-03 |
| SP-SNS-144 | Optical Sensor | 9 | 10 | 5 | PK-07 |

## supplier_otd_scorecard

| supplier | month | otd_pct | quality_ppm | contract_sla_pct |
|---|---|---|---|---|
| Shakti Components | 2026-10 | 81 | 940 | 95 |
| Delta Polymers | 2026-10 | 93 | 410 | 95 |
| Orion Metals | 2026-10 | 78 | 1020 | 95 |
