# Model Optimization — Hyperparameter Tuning & Regularization

Enhancing model performance using **Hyperparameter Tuning** and **Regularization**, and comparing baseline vs. optimized versions of multiple machine learning models using **Scikit-Learn**.

## 📌 Task

Enhance model performance using techniques such as **Hyperparameter Tuning** and **Regularization**. Compare the baseline and optimized versions of different models.

## 📊 Dataset

**Breast Cancer Wisconsin Dataset** (built into Scikit-Learn)

* **569 samples**
* **30 numerical features**
* **Target:** Malignant (0) or Benign (1)

## ⚙️ Approach

1. Loaded and prepared the dataset using a train/test split and feature scaling.
2. Trained baseline models using default hyperparameters:

   * Logistic Regression
   * Decision Tree
   * Support Vector Machine (SVM)
3. Applied **GridSearchCV** with **5-fold cross-validation** to tune the hyperparameters of each model.
4. Analyzed the effect of **regularization strength (`C`)** on Logistic Regression by comparing training and testing accuracy.
5. Visualized the relationship between regularization strength and model performance to understand **underfitting vs. overfitting**.
6. Evaluated the optimized models on the test dataset.
7. Compared **baseline vs. optimized** model performance.
8. Validated the best-performing final model using sample test cases.

## 📈 Results

### Best Hyperparameters Found

| Model                   | Best Parameters                                                  |
| ----------------------- | ---------------------------------------------------------------- |
| **Logistic Regression** | `C = 10`                                                         |
| **Decision Tree**       | `criterion = entropy`, `max_depth = 5`, `min_samples_split = 10` |
| **SVM**                 | `C = 1`, `gamma = scale`, `kernel = rbf`                         |

### Baseline vs. Optimized Performance

Hyperparameter tuning helped improve **model stability and generalization** by selecting better parameter combinations through cross-validation.

Among the optimized models, **SVM emerged as the best overall performer**.

## 🧠 Key Learnings

Through this task, I learned:

* How hyperparameters influence machine learning model performance.
* How to use **GridSearchCV** for systematic hyperparameter tuning.
* The importance of **5-fold cross-validation** when selecting model parameters.
* How regularization helps control model complexity.
* How different values of `C` can affect underfitting and overfitting.
* How to compare baseline and optimized models fairly.
* Why model optimization is an important step after building a baseline model.

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **Scikit-Learn**

  * `GridSearchCV`
  * `StandardScaler`
  * Logistic Regression
  * Decision Tree
  * SVM
* **Matplotlib**
* **Seaborn**

## 📂 Files

* `task3_model_optimization.ipynb` — Jupyter Notebook containing the complete workflow, model training, hyperparameter tuning, regularization analysis, visualizations, and results.

## ✍️ Author

**Kiran Shehzadi**
