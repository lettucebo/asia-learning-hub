# Trainer notes - seeded data-quality issues (Patient Cohort sheet)

Rows are Excel row numbers (header = row 1). Do not share with learners before the exercise.

| Excel row | Column | Issue | Recommended handling |
|---|---|---|---|
| 7 | Ward | Inconsistent label 'CARDIOLOGY' (standard: Cardiology) | Normalise to 'Cardiology' |
| 13 | Gender | Inconsistent value 'female' | Normalise to Female / Male |
| 14 | Ward | Inconsistent label 'cardiology' (standard: Cardiology) | Normalise to 'Cardiology' |
| 17 | Consent_To_Contact | Consent status missing | Treat as NO consent until confirmed |
| 21 | Discharge_Date | Date stored as text '2026/10/05' | Convert to a true date |
| 24 | Gender | Inconsistent value 'F' | Normalise to Female / Male |
| 26 | Gender | Inconsistent value 'male ' | Normalise to Female / Male |
| 28 | Post_Discharge_Contacts_30D | Text 'three' instead of number | Convert to 3 |
| 30 | Discharge_Date | Date stored as text '2026/10/13' | Convert to a true date |
| 40 | Primary_Diagnosis | Inconsistent diagnosis label 'CHF' | Normalise to 'Heart Failure' |
| 44 | Admit_Date | Admit date is after discharge date (negative LOS) | Verify admit/discharge dates |
| 53 | LOS_Days | Stored as text '5 days' | Convert to numeric days |
| 63 | Discharge_Date | Date stored as text '12-Oct-26' | Convert to a true date |
| 68 | LOS_Days | Stored as text '9 days' | Convert to numeric days |
| 70 | Discharge_Date | Missing discharge date | Obtain from ADT system |
| 74 | Consent_To_Contact | Consent status missing | Treat as NO consent until confirmed |
| 75 | Ward | Inconsistent label 'Pulmonary' (standard: Pulmonology) | Normalise to 'Pulmonology' |
| 78 | Primary_Diagnosis | Inconsistent diagnosis label 'Heart failure' | Normalise to 'Heart Failure' |
| 82 | Ward | Inconsistent label 'geriatrics' (standard: Geriatrics) | Normalise to 'Geriatrics' |
| 87 | Age | Missing age | Obtain from source system |
| 89 | Readmission_Risk_Score | Missing risk score | Recalculate or exclude from risk analysis |
| 91 | Ward | Inconsistent label 'pulmonology ' (standard: Pulmonology) | Normalise to 'Pulmonology' |
| 92 | Readmission_Risk_Score | Stored as text with trailing space | Convert to number |
| 95 | Ward | Inconsistent label 'Geriatric' (standard: Geriatrics) | Normalise to 'Geriatrics' |
| 103 | Primary_Diagnosis | Inconsistent diagnosis label 'T2DM' | Normalise to 'Type 2 Diabetes' |
| 104 | Readmission_Risk_Score | Score 130 is outside 0-100 range | Verify against scoring tool |
| 107 | Follow_Up_Booked | Missing value | Confirm with scheduling system before analysis |
| 109 | Age | Implausible age 0 for an adult ward | Verify against registration |
| 124 | Ward | Inconsistent label 'Gen Med' (standard: General Medicine) | Normalise to 'General Medicine' |
| 126 | Primary_Diagnosis | Inconsistent diagnosis label 'COPD exacerbation' | Normalise to 'COPD' |
| 130 | Ward | Inconsistent label 'Cardio ' (standard: Cardiology) | Normalise to 'Cardiology' |
| 132 | LOS_Days | Stored as text '5 days' | Convert to numeric days |
| 135 | Discharge_Date | Date stored as text '24-Oct-26' | Convert to a true date |
| 136 | Ward | Inconsistent label 'General Med.' (standard: General Medicine) | Normalise to 'General Medicine' |
| 153 | Readmission_Risk_Score | Stored as text with trailing space | Convert to number |
| 155 | Age | Implausible age 214 | Verify against registration; correct or mark unknown |
| 158 | Patient_ID | Duplicate of LH-P-1110 (row 111); all fields identical | Remove duplicate row after confirming with source system |
| 159 | Patient_ID | Duplicate of LH-P-1150 (row 151); all fields identical | Remove duplicate row after confirming with source system |
| 160 | Patient_ID | Duplicate of LH-P-1007 (row 8); all fields identical | Remove duplicate row after confirming with source system |
| 161 | Patient_ID | Duplicate of LH-P-1059 (row 60); all fields identical | Remove duplicate row after confirming with source system |

Total seeded issues: 40
