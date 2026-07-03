# Modeling Pipeline

## 1. Food Image Detection

The first modeling task reduces user effort: instead of manually entering meals, the user uploads a meal photo and the detection model identifies foods that can be mapped into nutrition records.

### Approach

- Model: YOLOv5.
- Food scope: Korean meal staples represented in the collected dataset.
- Training setup preserved in project notes: batch size 16, epoch 200.
- Evaluation target: mAP at IoU 0.5.
- Reported project result: mAP 0.94.

### Artifacts

- `notebooks/01_yolov5_food_detection.ipynb`
- `notebooks/02_yolo_label_conversion.ipynb`
- `src/yolov5_data.yaml`
- `artifacts/models/yolov5_food_detection_best.pt`
- `artifacts/images/pr_curve.png`

### Public Review Notes

- Presentation notes describe a 20-food dataset.
- The preserved `src/yolov5_data.yaml` lists 22 label names, so this file should be read as an experiment configuration artifact rather than a fresh claim about final service scope.
- `artifacts/models/yolov5_food_detection_best.pt` is larger than 50 MB and should be reviewed for Git LFS or external release storage before public push approval.

## 2. Nutrition Aggregation

Detected foods are mapped to food-nutrition data to calculate intake totals. The service concept split the user flow into three time windows:

- EveryHI: daily meal and nutrition-balance check.
- WeekHI: weekly cumulative meal record and disease-risk prediction.
- MonthHI: monthly cumulative meal record, disease-risk prediction, and insurance recommendation.

The public repository documents this flow, but the original nutrition source tables are excluded.

## 3. Disease-Risk Prediction

The disease-risk model uses Korean National Health and Nutrition Examination Survey-derived variables to learn relationships between nutrition intake and disease labels.

### Inputs

- 23 nutrition intake variables.
- Age.
- Sex.

### Modeling Strategy

- Disease labels were imbalanced, so SMOTE was applied.
- Multiple classifiers were explored, including logistic regression and random forest.
- Stratified k-fold cross-validation was used during experimentation.
- XGBoost was selected as the final model in the preserved project notes.

### Artifacts

- `notebooks/03_disease_prediction_model.ipynb`
- `notebooks/04_everyhi_insurance_recommendation.ipynb`

## Evidence and Reproducibility Boundary

- Reported detection evidence is the preserved project result: mAP 0.94 at IoU 0.5, plus `artifacts/images/pr_curve.png`.
- Disease-risk modeling can be inspected through notebooks and documented feature strategy, but full retraining is blocked in the public repo because the original survey and nutrition-source data are excluded.
- Model output should be interpreted as a prototype risk signal. It is not medical advice, insurance underwriting evidence, or a production scoring system.
