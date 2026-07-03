# Retrospective

## What Worked

- The project connected a realistic user habit, meal photos, to a difficult insurance-discovery problem.
- The pipeline joined food detection, nutrition aggregation, disease-risk prediction, and insurance-product matching into one service flow.
- SMOTE and stratified validation were considered because disease labels were imbalanced.
- The recommendation layer used disease-coverage rules, which made the prototype easier to explain than an opaque ranking model.

## Technical Tradeoffs

- YOLOv5 was practical for detecting multiple foods in one image, but the project scope was limited to foods represented in the collected dataset.
- Notebook-first experimentation helped during competition work, but it limited later reproducibility and modular reuse.
- Rule-based insurance matching was transparent, but it did not cover premiums, underwriting rules, exclusions, or policy-term freshness.

## Public Repository Constraints

- Raw datasets and team-private materials are excluded, so public retraining is intentionally not promised.
- The repository still contains a model file above 50 MB and an insurance-product `.xls` artifact that require review before a clean public push decision.
- Preserved notebooks may contain paths or assumptions from the original experiment environment.

## What I Would Improve

- Split preprocessing, training, inference, and recommendation into CLI commands or pipeline modules.
- Replace the large tracked model with Git LFS or a release asset.
- Replace the insurance-product spreadsheet with a clearly licensed public sample schema if redistribution is not confirmed.
- Add structured model-comparison tables, confusion matrices, and reproducible experiment metadata.
- Build a small web or mobile prototype to validate the real user flow.

## Reviewer Notes

Read this project as an insurtech AI/data PoC, not as a production health or insurance system. The strongest evidence is the end-to-end pipeline design, preserved detection result, feature strategy, and inspectable recommendation rule.
