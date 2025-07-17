# Medical Datasets for Master-Seminar: AI for Vision-Language Models in Medical Imaging (IN2107, IN45069)

This repository provides medical imaging datasets for the Master-Seminar course **AI for Vision-Language Models in Medical Imaging (IN2107, IN45069)**. These datasets are designed to support project work and poster sessions.

## 📊 Available Datasets

### 1. Chest X-rays Dataset 
- **Samples**: 50 images

### 2. NOVA Brain MRI Dataset  
- **Cases**: 25 clinical records

## 🎯 Tasks & Evaluation

### 🫁 Chest X-rays Analysis

1. **Classification Task**
    ```text
    Input: X-ray image
    Goal: Classify as 'healthy' or 'unhealthy'
    Prompt: "Given the medical image, classify it as 'healthy' or 'unhealthy'."
    Evaluation: Accuracy/F1 using `scripts/evaluate_metrics.py`
    ```

2. **Abnormality Grounding**
    ```text
    Input: X-ray image
    Goal: Locate specific abnormality areas
    Prompt: "Please locate {disease} and output the bounding boxes."
    Evaluation: mAP using `scripts/calculate_map.py`
    ```

### 🧠 Brain MRI Analysis

1. **Description Generation**
    ```text
    Input: MRI slice
    Goal: Generate medical description
    Prompt: "Please describe the given medical image."
    Evaluation: BLEU score using `scripts/calculate_bleu.py`
               LLM evaluation: "Given the ground truth sentence and predicted sentence, determine whether it is correct or not."
    ```

2. **Abnormality Detection**
    ```text
    Input: MRI slice
    Goal: Identify abnormal regions
    Prompt: "Please locate any abnormal areas in the MRI image and output the bounding boxes."
    Evaluation: mAP using `scripts/calculate_map.py`
    ```

3. **Disease Diagnosis** (Optional)
    ```text
    Input: Clinical history + Image findings
    Goal: Predict disease
    Prompt: "Based on the clinical history: {clinical history} and image findings: {slice1: ..., slice2: ...}, provide your diagnosis for the disease."
    Evaluation: LLM evaluation: "Given the predicted diagnosis and ground truth diagnosis, determine whether it is correct or not."
    ```

## 📝 Implementation Guidelines

1. Refer to `instruction.ipynb` for dataset loading instructions.
2. Customize prompts as needed for your tasks.
3. Ensure consistent output formats across tasks.
4. Use appropriate evaluation metrics:
    - **Text**: BLEU (`scripts/calculate_bleu.py`) or **using LLMs to evluate**.
    - **Classification**: Accuracy/F1 (`scripts/evaluate_metrics.py`)
    - **Detection**: mAP (`scripts/calculate_map.py`)
5. When using LLMs for evaluating open-ended responses, design detailed and reasonable prompts. The provided examples are basic illustrations.

## ⚠️ Notes
- Prompts are customizable to fit specific requirements.
- Consistent output formats are essential for reproducibility.
- **Different LLMs may produce varying bounding box formats; ensure compatibility.**

## 📚 References

[1] Nguyen, H. Q., Lam, K., Le, L. T., Pham, H. H., Tran, D. Q., Nguyen, D. B., ... & Vu, V. (2022). VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations. Scientific Data, 9(1), 429.

[2] Bercea, C. I., Li, J., Raffler, P., Riedel, E. O., Schmitzer, L., Kurz, A., ... & Wiestler, B. (2025). NOVA: A Benchmark for Anomaly Localization and Clinical Reasoning in Brain MRI. arXiv preprint arXiv:2505.14064.
