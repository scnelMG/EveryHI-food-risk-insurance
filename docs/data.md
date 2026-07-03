# Data and Public-Safety Policy

This document separates project evidence from material that should not be treated as public portfolio content. The repository is intended for inspection of the EveryHI AI/data pipeline, not redistribution of raw datasets or private competition materials.

## Data Inputs

| Data | Purpose | Public repository handling |
| --- | --- | --- |
| Food image data | YOLOv5 food object-detection training | Raw source stays in local archive or excluded source storage, not in the public repo |
| Food label data | Bounding-box training labels | Raw labels are excluded; conversion logic is kept in `src/` |
| Korean National Health and Nutrition Examination Survey data | Nutrition-based disease-risk modeling | Raw survey data is excluded; feature strategy is documented only |
| Food-nutrition source data | Mapping detected foods to nutrient totals | Original source tables are excluded; pipeline behavior is documented |
| Disease-insurance product data | Matching high-risk diseases to covered products | `artifacts/data/disease_insurance_products.xls` exists but must be reviewed before public-release approval |

## Food Detection Dataset

- Project notes describe 20 selected food categories.
- Roughly 300 images per food class were collected for the project dataset.
- Sources included AI Hub and web-crawled food images.
- Food regions were labeled with bounding boxes for object detection.
- Training and test data were split at train:test = 8:2.

## Disease-Risk Dataset

- The model used nutrition and health-check variables from the Korean National Health and Nutrition Examination Survey.
- Inputs were 23 nutrition variables plus age and sex.
- Target labels covered eight disease categories, including hypertension, dyslipidemia, and stroke.
- SMOTE was used to address class imbalance in disease labels.

## Public-Safe Boundary

The following materials must not be published directly in the GitHub repo:

- Participant forms, team-private documents, or files with personal information.
- Korean National Health and Nutrition Examination Survey raw data.
- Full crawled image sets and raw bounding-box labels.
- Duplicate zip files, large raw datasets, and Drive archives.
- Unrelated research materials from other projects.
- Copied `.git` folders, `.env` files, credentials, and notebook checkpoints.

## Existing Publication Blockers

These files already exist in the repository and were not duplicated or modified during portfolio documentation work. They must be reviewed before treating the repo as a clean push/publication candidate.

| File | Current reason for review | Required decision |
| --- | --- | --- |
| `artifacts/models/yolov5_food_detection_best.pt` | 57,097,482 bytes, above the 50 MB portfolio threshold | Move to Git LFS or external release storage, or explicitly approve keeping the model in Git history |
| `artifacts/data/disease_insurance_products.xls` | Insurance-product spreadsheet with redistribution/proprietary-content risk by name and domain | Confirm it contains only public-safe product fields and no restricted, private, or licensed source material |

## Inspection and Reproduction Boundary

The public repository supports review of data design, feature flow, notebook order, representative artifacts, and recommendation logic. It does not support a clean end-to-end retraining run because the raw food-image dataset, original nutrition source data, and original health-survey data are excluded.
