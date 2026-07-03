# EveryHI - 식단 기반 질병 위험 보험 추천

> 식단 이미지 분석으로 영양 섭취 패턴을 추정하고, 질병 위험 신호와 보험 보장 항목을 연결한 인슈어테크 PoC입니다.

[![Python](https://img.shields.io/badge/Python-ML%20Pipeline-3776AB?logo=python&logoColor=white)](requirements.txt)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-Food%20Detection-00FFFF)](src/yolov5_data.yaml)
[![XGBoost](https://img.shields.io/badge/XGBoost-Risk%20Model-FF6600)](docs/modeling.md)
[![Portfolio](https://img.shields.io/badge/Portfolio-Public%20Safe-2ea44f)](docs/project-brief.md)

## 개요

EveryHI는 사용자가 촬영한 식단 사진을 바탕으로 음식 종류를 탐지하고, 영양 정보를 집계한 뒤, 질병 위험 신호와 보험 상품의 보장 질병을 매칭하는 팀 프로젝트입니다. 이 저장소는 전체 서비스 구현물이 아니라, 공개 가능한 AI/데이터 파이프라인과 기술적 의사결정을 검토할 수 있도록 정리한 포트폴리오 버전입니다.

이 프로젝트는 의료 진단, 보험 심사, 보험료 산정, 투자/금융 조언을 목적으로 하지 않습니다.

## 빠른 검토 경로

| 먼저 볼 것 | 확인할 내용 |
| --- | --- |
| [docs/project-brief.md](docs/project-brief.md) | 문제 정의, 역할 범위, 포트폴리오 관점의 검토 포인트 |
| [docs/modeling.md](docs/modeling.md) | 음식 탐지, 영양 변수, 질병 위험 모델링 흐름 |
| [docs/data.md](docs/data.md) | 공개 가능 자료와 비공개/제외 자료의 경계 |
| [docs/recommendation.md](docs/recommendation.md) | 보험 보장 항목 매칭 로직 |
| [src/recommendation.py](src/recommendation.py) | 규칙 기반 추천 구현 예시 |

## 문제 정의

20대 사용자는 식단이나 건강 습관을 기록하더라도, 본인의 생활 패턴과 보험 보장 항목을 연결해 이해하기 어렵습니다. EveryHI는 식단 기록을 보험 탐색의 진입점으로 사용할 수 있는지 검증했습니다.

- 식단 사진에서 여러 음식 객체를 탐지합니다.
- 탐지된 음식을 영양 정보로 변환하고 기간별로 집계합니다.
- 영양 변수, 나이, 성별을 활용해 질병 위험 신호를 추정합니다.
- 위험 신호와 보험 상품의 보장 질병을 연결해 추천 사유를 설명합니다.

## 내 역할

팀 프로젝트 산출물이며, 이 README는 단독 제작을 주장하지 않습니다. 공개 포트폴리오에서 설명 가능한 기여 범위는 다음과 같습니다.

- 음식 클래스 정의, 이미지 수집 흐름, YOLO 라벨 변환 및 탐지 파이프라인 정리
- 영양 변수 기반 질병 위험 모델링 실험과 XGBoost 선택 근거 문서화
- 보험 추천 로직을 설명 가능한 규칙 기반 구조로 정리
- 원본 데이터, 팀 내부 자료, 대용량 모델 artifact를 제외한 공개 안전성 정리

## 기술적 의사결정

| 영역 | 선택 | 이유 |
| --- | --- | --- |
| 음식 인식 | YOLOv5 객체 탐지 | 한 장의 식단 사진에 여러 음식이 포함될 수 있어 단일 분류보다 객체 탐지가 적합합니다. |
| 질병 위험 모델 | 영양 변수 + 인구통계 변수 + XGBoost | 표 형태의 영양/건강 변수를 다루고 feature importance를 검토하기 쉽습니다. |
| 클래스 불균형 | SMOTE, stratified validation | 질병 라벨 불균형으로 인한 다수 클래스 편향을 줄이기 위한 선택입니다. |
| 보험 추천 | 규칙 기반 필터링 | 추천 결과의 이유를 사람이 검토할 수 있도록 블랙박스 랭킹을 피했습니다. |

## 파이프라인

```mermaid
flowchart LR
    A["식단 사진"] --> B["YOLOv5 음식 탐지"]
    B --> C["음식-영양 정보 매핑"]
    C --> D["일/주/월 단위 영양 집계"]
    D --> E["질병 위험 모델"]
    E --> F["고위험 질병 후보"]
    F --> G["보험 보장 항목 매칭"]
```

## 결과 근거

- 프로젝트 산출물 기준 YOLOv5 학습 설정: batch size 16, 200 epochs
- 프로젝트 artifact 기준 mAP 0.94 at IoU 0.5
- 질병 위험 모델 입력: 23개 영양 변수, 나이, 성별
- 추천 로직: 질병 위험 후보와 보험 보장 항목의 explainable matching
- 대표 결과 이미지: [artifacts/images/pr_curve.png](artifacts/images/pr_curve.png)

원본 데이터와 전체 학습 artifact는 공개 저장소에 포함하지 않았기 때문에, 이 저장소의 결과는 재현 가능한 production benchmark가 아니라 포트폴리오 검토용 근거입니다.

## 재현 가능성

```bash
pip install -r requirements.txt
```

공개 checkout에서 확인 가능한 것:

- `docs/`의 설계와 모델링 근거
- `notebooks/`의 실험 흐름
- `src/`의 라벨 변환, 탐지 설정, 추천 로직

공개 checkout에서 완전 재현이 어려운 것:

- 원본 음식 이미지와 라벨이 필요한 YOLO 재학습
- 원본 영양/건강 데이터가 필요한 질병 위험 모델 재학습
- 실제 보험 약관, 보험료, 인수 기준을 반영한 상품 추천

## 공개/비공개 경계

공개 저장소에는 검토 가능한 문서, 소스 코드, 일부 결과 이미지, 노트북만 남겼습니다. 원본 이미지, 원천 데이터, 팀 내부 문서, 개인정보, 대용량 모델, Drive archive, `.git` 복사본은 GitHub 공개 대상에서 제외했습니다.

## 한계

- 질병 위험 모델은 PoC이며 진단이나 보험 심사에 사용할 수 없습니다.
- 추천 로직은 보장 질병명 기반 매칭이며 실제 보험 약관의 예외, 대기기간, 보험료, 가입 가능성을 판단하지 않습니다.
- 노트북은 실험 기록 성격이 강하며, 일부 실행은 제외된 로컬 데이터에 의존합니다.
- 서비스 UI는 개념 검증 단계이며 production app은 포함되어 있지 않습니다.
