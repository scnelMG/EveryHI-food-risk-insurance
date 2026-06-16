# EveryHI

식단 이미지 분석 기반 질병 예측 및 보험 추천 서비스

EveryHI는 보험에 관심이 낮지만 건강관리에 익숙한 20대를 대상으로, 매일 찍는 식단 사진을 건강 기록으로 전환하고 누적된 영양 데이터를 바탕으로 질병 위험과 관련 보험을 추천하는 인슈어테크 서비스 기획/AI PoC 프로젝트입니다.

> 팀 공모전 프로젝트이며, 이 저장소는 포트폴리오 공개를 위해 AI/데이터 파이프라인 중심으로 재정리했습니다.

## 핵심 아이디어

1. 사용자가 식단 사진을 등록합니다.
2. YOLOv5 모델이 이미지 속 음식을 인식합니다.
3. 음식별 영양성분을 누적해 일/주/월 단위 섭취 데이터를 만듭니다.
4. XGBoost 기반 질병 예측 모델이 고위험 질병을 추정합니다.
5. 예측된 위험 질병을 보장하는 보험상품을 rule-based filtering으로 추천합니다.

## 주요 성과

| 영역 | 내용 |
| --- | --- |
| 음식 인식 | 20종 음식 데이터셋 구축, 음식별 약 300장 수집 및 라벨링 |
| 객체 탐지 | YOLOv5 학습, train:test = 8:2, batch size 16, epoch 200 |
| 성능 지표 | IoU 0.5 기준 mAP 0.94 |
| 질병 예측 | 국민건강영양조사 기반 23개 영양소 + 나이/성별 입력 |
| 불균형 대응 | SMOTE oversampling 적용 |
| 최종 모델 | XGBoost 분류 모델 |
| 보험 추천 | 위험 질병과 질병보험 보장 항목을 매칭하는 rule-based filtering |

## 서비스 구조

```mermaid
flowchart LR
    A["식단 사진"] --> B["YOLOv5 음식 인식"]
    B --> C["음식별 영양소 매핑"]
    C --> D["일/주/월 섭취량 집계"]
    D --> E["XGBoost 질병 위험 예측"]
    E --> F["위험군 판단"]
    F --> G["질병보험 상품 추천"]
```

## Repository Structure

```text
.
├── artifacts/
│   ├── data/               # 공개 가능한 보험상품 데이터
│   ├── images/             # 대표 결과 이미지
│   ├── models/             # 선별 보존 모델 파일, Git LFS 후보
│   └── presentations/      # 최종 발표자료
├── docs/
│   ├── data.md             # 데이터셋과 공개/비공개 기준
│   ├── modeling.md         # 음식 인식 및 질병 예측 파이프라인
│   ├── recommendation.md   # 보험 추천 로직
│   └── retrospective.md    # 회고 및 개선점
├── notebooks/
│   ├── 01_yolov5_food_detection.ipynb
│   ├── 02_yolo_label_conversion.ipynb
│   ├── 03_disease_prediction_model.ipynb
│   └── 04_everyhi_insurance_recommendation.ipynb
└── src/
    ├── detect_yolov5.py
    ├── extract_food.py
    ├── recommendation.py
    ├── translabel.py
    └── yolov5_data.yaml
```

`archive/`에는 공개 저장소 루트에 두기 부적합한 원본 자료, 대용량 데이터, 중복 파일, 초안 문서를 보존했습니다. 이 폴더는 `.gitignore`로 제외됩니다.

## 발표자료와 결과물

- [최종 발표자료](artifacts/presentations/EveryHI_final_presentation.pptx)
- [PR curve](artifacts/images/pr_curve.png)
- [질병보험 상품 데이터](artifacts/data/disease_insurance_products.xls)

## AI/데이터 기여 포인트

- 식단 이미지 객체 탐지를 위한 음식 클래스 정의, 이미지 수집/정제, 라벨 변환 흐름 정리
- YOLOv5 학습 데이터 구성과 성능 지표 정리
- 국민건강영양조사 기반 질병 예측 입력 변수 설계
- 질병 유무 데이터의 클래스 불균형 문제를 SMOTE로 보정
- 예측 질병과 질병보험 보장 항목을 연결하는 추천 규칙 설계
- 공모전 발표자료를 기준으로 공개 가능한 포트폴리오 구조 재정리

## 실행 환경

노트북 원본은 공모전 당시의 실험 기록을 보존합니다. 대용량 원자료는 공개 저장소에서 제외되어 있으므로, 전체 재학습보다는 파이프라인 이해와 코드 리뷰 목적에 맞춰 정리했습니다.

```bash
pip install -r requirements.txt
python -m src.recommendation
```

## 공개 범위

Public 포트폴리오에서는 개인정보, 팀 내부 초안, 원천 대용량 데이터, 크롤링 원본, 제출 서류를 제외합니다. 필요한 원본은 로컬 `archive/`에 보존하고, 공개 저장소에는 핵심 산출물과 재현 가능한 설명만 남깁니다.
