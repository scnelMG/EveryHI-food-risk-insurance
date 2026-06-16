"""Rule-based insurance recommendation example for EveryHI.

The real competition data was collected from insurance product pages. This
module keeps the recommendation policy readable for portfolio review.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DiseaseRisk:
    name: str
    probability: float
    threshold: float

    @property
    def is_high_risk(self) -> bool:
        return self.probability >= self.threshold


@dataclass(frozen=True)
class InsuranceProduct:
    company: str
    product_name: str
    covered_diseases: tuple[str, ...]


def recommend_products(
    risks: list[DiseaseRisk],
    products: list[InsuranceProduct],
) -> list[tuple[InsuranceProduct, float, tuple[str, ...]]]:
    """Rank products by covered high-risk diseases and total risk score."""

    high_risk_scores = {
        risk.name: risk.probability
        for risk in risks
        if risk.is_high_risk
    }

    ranked: list[tuple[InsuranceProduct, float, tuple[str, ...]]] = []
    for product in products:
        matched = tuple(
            disease
            for disease in product.covered_diseases
            if disease in high_risk_scores
        )
        if not matched:
            continue

        score = sum(high_risk_scores[disease] for disease in matched)
        ranked.append((product, score, matched))

    return sorted(ranked, key=lambda item: (len(item[2]), item[1]), reverse=True)


def _demo() -> None:
    risks = [
        DiseaseRisk("고혈압", 0.72, 0.55),
        DiseaseRisk("당뇨병", 0.49, 0.60),
        DiseaseRisk("이상지질혈증", 0.68, 0.50),
    ]
    products = [
        InsuranceProduct("A손해보험", "건강든든 질병보험", ("고혈압", "당뇨병")),
        InsuranceProduct("B생명", "생활습관 케어보험", ("이상지질혈증", "고혈압")),
        InsuranceProduct("C화재", "암 집중 보장보험", ("위암", "폐암")),
    ]

    for product, score, matched in recommend_products(risks, products):
        diseases = ", ".join(matched)
        print(f"{product.company} | {product.product_name} | {score:.2f} | {diseases}")


if __name__ == "__main__":
    _demo()
