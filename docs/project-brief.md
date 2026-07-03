# Project Brief

## Problem

EveryHI connects a familiar behavior, taking meal photos, to a hard-to-compare domain: disease-insurance discovery. The service concept asks whether repeated diet records can become a personal risk context for explaining which disease-insurance products may be relevant.

## User or Stakeholder

- Primary user: people in their 20s who are comfortable tracking health habits but are not actively comparing insurance products.
- Review stakeholder: portfolio reviewers who need to see data-science judgment, service framing, and publication-safety discipline.
- Domain stakeholder: insurance or health-product teams evaluating whether the concept is explainable enough for a prototype.

## Role and Contribution

This was a team competition project. The public repository presents the parts I can safely stand behind for portfolio review:

- AI/data pipeline framing from meal photo to nutrition record to disease-risk signal.
- YOLOv5 food-detection setup, label conversion workflow, and model-result documentation.
- Disease-risk modeling notes using nutrition variables, age, sex, SMOTE, stratified validation, and XGBoost.
- Rule-based insurance-product matching that keeps recommendation reasons inspectable.
- Public-safe curation of README, docs, notebooks, artifacts, and blocker evidence.

It does not claim sole authorship of all team planning, presentation, or submission materials.

## Repository Review Path

1. `README.md` - service summary, role, evidence, public-safety boundary.
2. `docs/modeling.md` - food detection, nutrition aggregation, and disease-risk modeling.
3. `docs/recommendation.md` - rule-based coverage matching and demo blocker notes.
4. `docs/data.md` - data sources, excluded materials, and publish blockers.
5. `notebooks/` - preserved experiment records.
6. `src/recommendation.py` - inspectable recommendation example; the module-level demo is currently blocked by malformed string literals.

## Public-Safe Artifacts

- `artifacts/images/pr_curve.png`
- `artifacts/presentations/EveryHI_final_presentation.pptx`
- `notebooks/*.ipynb` as experiment records
- `src/*.py` and `src/yolov5_data.yaml` as inspectable implementation artifacts
- `docs/*.md` as public review documentation

## Excluded Materials

- Raw food images and bounding-box label corpora.
- Korean National Health and Nutrition Examination Survey raw data and original food-nutrition source data.
- Crawled raw materials, Drive archives, zip files, copied `.git` folders, and local `archive/` contents.
- Team-private drafts, forms, signed/private documents, and personal information.
- Credentials, `.env` files, and notebook checkpoints.

## Evidence and Results

- YOLOv5 detection experiment documented as batch size 16, 200 epochs, train:test 8:2, and mAP 0.94 at IoU 0.5 in the preserved project artifact.
- Food dataset design documented as 20 food categories with roughly 300 images per class in the project notes.
- Disease-risk model feature strategy documented as 23 nutrition variables plus age and sex.
- Recommendation behavior can be inspected through `src/recommendation.py`, but the module-level demo is not currently verified as runnable.

## Reproducibility

The current repository is inspection-first. The command `python -m src.recommendation` is currently unverified and blocked by malformed demo string literals in `src/recommendation.py`.

```bash
pip install -r requirements.txt
```

Full model retraining is intentionally not promised because original raw data and some source materials are excluded from the public repo.

## Limitations

- Prototype disease-risk output is not medical advice, underwriting evidence, or financial advice.
- The insurance matching layer is rule-based and does not validate current premiums, exclusions, waiting periods, policy terms, or eligibility.
- Existing artifacts include one file over 50 MB and one insurance-product spreadsheet that must be reviewed before a clean public push decision.
