# Supervised Learning Models Comparison

Implementation and comparison of multiple supervised learning algorithms for a binary classification problem, built with *Scikit-Learn*.

## 📌 Task

Implement and compare multiple supervised learning algorithms (Logistic Regression, Decision Tree, SVM) on a classification problem using Scikit-Learn.

## 📊 Dataset

*Breast Cancer Wisconsin Dataset* (built into Scikit-Learn)
- 569 samples, 30 numerical features
- Target: Malignant (0) or Benign (1)

## ⚙️ Approach

1. Loaded and inspected the dataset (no missing values)
2. Split data into train/test sets (80/20)
3. Scaled features using StandardScaler
4. Trained three classification models:
   - Logistic Regression
   - Decision Tree
   - Support Vector Machine (SVM)
5. Evaluated each model using Accuracy, Precision, Recall, and F1-Score
6. Validated the best model on sample test cases

## 📈 Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| *SVM* | 0.982 | 0.973 | 1.000 | 0.986 |
| Logistic Regression | 0.974 | 0.972 | 0.986 | 0.979 |
| Decision Tree | 0.947 | 0.958 | 0.958 | 0.958 |

*Best performing model: SVM*, achieving ~98% accuracy on unseen test data.

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-Learn

## 📂 Files

- task2_supervised_models.ipynb — Jupyter notebook with full workflow and outputs

## ✍️ Author

Kiran Shehzadi