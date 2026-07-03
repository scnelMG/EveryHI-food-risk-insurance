# Insurance Recommendation

## Goal

The recommendation layer takes high-risk disease outputs from the disease-risk model and ranks disease-insurance products that cover those diseases.

## Recommendation Flow

1. Feed monthly average nutrition totals and user attributes into the disease-risk model.
2. Estimate disease-level risk probabilities.
3. Set disease-specific high-risk thresholds using the project's recall/precision tradeoff.
4. Match high-risk diseases to insurance-product coverage fields.
5. Rank matching products by number of covered high-risk diseases and total high-risk score.

## Rule-Based Filtering

This project intentionally used an explainable rule-based filter instead of a complex recommender system.

- Input: disease-level risk scores and disease-insurance product data.
- Rule: prioritize products covering the user's high-risk diseases.
- Ranking criteria: covered high-risk disease count, then sum of matched disease-risk scores.
- Benefit: recommendation reasons can be explained in a competition prototype.
- Limitation: premiums, eligibility, exclusions, waiting periods, and current policy terms require additional verified product data.

The inspectable example implementation is in `src/recommendation.py`.

## Public Review Notes

- The demo implementation uses `DiseaseRisk` and `InsuranceProduct` dataclasses so the ranking rule can be inspected without private data.
- The command `python -m src.recommendation` is currently unverified and blocked by malformed demo string literals in `src/recommendation.py`; treat this as source-inspection evidence until the demo literals are repaired.
- The approach is not a licensed insurance recommendation system and must not be presented as financial advice.
