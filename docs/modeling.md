# Modeling Pipeline

## 1. 음식 이미지 인식

목표는 사용자가 매번 직접 식단을 입력해야 하는 번거로움을 줄이는 것입니다. 식단 사진을 업로드하면 객체 탐지 모델이 음식명을 인식하고, 이후 영양소 계산 단계로 연결됩니다.

### 접근

- 모델: YOLOv5
- 클래스: 잡곡밥, 김치찌개, 된장찌개, 라면 등 20종 음식
- 학습 조건: batch size 16, epoch 200
- 평가: IoU 0.5 기준 mAP
- 발표자료 성과: mAP 0.94

### 산출물

- `notebooks/01_yolov5_food_detection.ipynb`
- `notebooks/02_yolo_label_conversion.ipynb`
- `src/yolov5_data.yaml`
- `artifacts/models/yolov5_food_detection_best.pt`
- `artifacts/images/pr_curve.png`

## 2. 영양소 집계

음식 인식 결과를 음식별 영양성분 데이터와 매핑해 하루 단위 섭취량을 계산합니다. 서비스 기획상 EveryHI, WeekHI, MonthHI로 기능을 나눴습니다.

- EveryHI: 하루 식단과 영양 불균형 확인
- WeekHI: 일주일 누적 식단 기반 질병 예측
- MonthHI: 한 달 누적 식단 기반 질병 예측 및 보험 추천

## 3. 질병 예측

질병관리청 국민건강영양조사 데이터를 바탕으로 영양소 섭취량과 질병 유무의 관계를 학습합니다.

### 입력 변수

- 23개 영양소 섭취량
- 나이
- 성별

### 모델링 전략

- 질병 유무 데이터는 클래스 불균형이 커서 SMOTE를 적용
- 로지스틱 회귀, 랜덤포레스트 등 여러 분류 모델 실험
- Stratified k-fold 교차검증 수행
- 최종 모델은 XGBoost로 선정

### 산출물

- `notebooks/03_disease_prediction_model.ipynb`
- `notebooks/04_everyhi_insurance_recommendation.ipynb`
