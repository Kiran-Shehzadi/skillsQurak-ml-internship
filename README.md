# 🤖 Machine Learning Internship — Task Portfolio

A collection of hands-on machine learning projects completed during my **Machine Learning Internship at SkillSquark**.

This repository documents my practical learning journey, covering **data cleaning, exploratory data analysis, preprocessing, supervised learning, model evaluation, hyperparameter tuning, and regularization** using Python and Scikit-Learn.

---

## 📌 Internship Tasks Overview

| Task  | Project                               | Dataset                         | Key Skills                                                                | Status      |
| ----- | ------------------------------------- | ------------------------------- | ------------------------------------------------------------------------- | ----------- |
| **1** | EDA & Data Preprocessing              | Titanic Dataset                 | Data Cleaning, EDA, Missing Value Imputation, Encoding, Outlier Treatment | ✅ Completed |
| **2** | Supervised Learning Models Comparison | Breast Cancer Wisconsin Dataset | Classification, Feature Scaling, Model Training, Model Evaluation         | ✅ Completed |
| **3** | Model Optimization                    | Breast Cancer Wisconsin Dataset | Hyperparameter Tuning, Regularization, GridSearchCV, Cross-Validation     | ✅ Completed |

---

# 📊 Task 1 — Exploratory Data Analysis & Preprocessing

## 🎯 Objective

Perform Exploratory Data Analysis (EDA) and prepare the **Titanic dataset** for machine learning by identifying data quality issues, handling missing values, encoding categorical variables, and treating outliers.

## ⚙️ Approach

### 1. Data Inspection

* Examined dataset structure, shape, data types, and summary statistics.
* Identified important features and potential data quality issues.

### 2. Missing Value Analysis

* Quantified missing values across columns.
* Visualized missing data using a heatmap.
* Found significant missing values in:

  * `Age`
  * `Cabin`
  * `Embarked`

### 3. Exploratory Data Analysis

Performed:

* Univariate analysis
* Bivariate analysis
* Histograms
* Value counts
* Correlation analysis
* Boxplots

This helped identify relationships between features and the target variable `Survived`.

### 4. Data Cleaning

* Imputed `Age` using the median.
* Imputed `Embarked` using the mode.
* Removed `Cabin` because of excessive missing values.
* Removed non-predictive identifier columns such as:

  * `Name`
  * `Ticket`
  * `PassengerId`
* Checked for and removed duplicate records.

### 5. Feature Encoding

* Converted `Sex` into a numerical representation.
* Applied one-hot encoding to `Embarked`.

### 6. Outlier Treatment

* Identified outliers in the `Fare` feature using boxplots.
* Applied the IQR method to cap extreme values while preserving the records.

### 7. Validation & Export

Verified that the processed dataset was:

* Fully numerical
* Free from missing values
* Suitable for machine learning

The cleaned dataset was exported for further use.

## 💡 Key Learnings

* Learned how to systematically inspect and clean a real-world dataset.
* Understood how missing data can affect machine learning models.
* Practiced categorical feature encoding.
* Learned how to identify and handle outliers using the IQR method.
* Understood the importance of preprocessing before model training.

## 📂 Task 1 Files

| File                         | Description                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| `README.md`                  | Task documentation                                          |
| `Task1_EDA_Preprocessing.py` | Python script containing the EDA and preprocessing workflow |
| `Task1_Report.txt`           | Task report and observations                                |
| `cleaned_data.csv`           | Processed dataset                                           |
| `output.csv`                 | Generated output data                                       |
| `eda_visualization.png`      | EDA visualization                                           |

## 🛠️ Tools

**Python · Pandas · NumPy · Matplotlib · Seaborn**

---

# 🧠 Task 2 — Supervised Learning Models Comparison

## 🎯 Objective

Implement and compare multiple supervised learning algorithms for a **binary classification problem** using Scikit-Learn.

The models used were:

* Logistic Regression
* Decision Tree
* Support Vector Machine (SVM)

## 📊 Dataset

**Breast Cancer Wisconsin Dataset** built into Scikit-Learn.

* **569 samples**
* **30 numerical features**
* **Target:** Malignant (0) or Benign (1)

## ⚙️ Approach

### 1. Dataset Preparation

* Loaded and inspected the dataset.
* Verified that there were no missing values.

### 2. Train/Test Split

Split the dataset into:

* **80% training data**
* **20% testing data**

This allowed the models to be evaluated on unseen data.

### 3. Feature Scaling

Applied `StandardScaler` to standardize the numerical features.

Feature scaling was particularly important for models such as **SVM and Logistic Regression**.

### 4. Model Training

Trained and compared:

* Logistic Regression
* Decision Tree
* Support Vector Machine (SVM)

### 5. Model Evaluation

Evaluated each model using:

* Accuracy
* Precision
* Recall
* F1-Score

### 6. Model Validation

Tested the best-performing model using sample test cases to verify its predictions.

## 📈 Results

| Model               |  Accuracy | Precision |    Recall |  F1 Score |
| ------------------- | --------: | --------: | --------: | --------: |
| **SVM**             | **0.982** |     0.973 | **1.000** | **0.986** |
| Logistic Regression |     0.974 |     0.972 |     0.986 |     0.979 |
| Decision Tree       |     0.947 |     0.958 |     0.958 |     0.958 |

### 🏆 Best Performing Model

**SVM** achieved the best overall performance with approximately **98.2% accuracy** on the unseen test data.

## 💡 Key Learnings

Through this task, I learned how to:

* Build supervised machine learning models.
* Prepare data for classification.
* Apply feature scaling using `StandardScaler`.
* Compare multiple algorithms on the same dataset.
* Evaluate models using multiple performance metrics.
* Understand why different algorithms can produce different results.
* Evaluate model performance on unseen data.

## 📂 Task 2 Files

| File                            | Description                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| `README.md`                     | Task documentation                                                                     |
| `task2_supervised_models.ipynb` | Complete notebook containing preprocessing, model training, evaluation, and comparison |

## 🛠️ Tools

**Python · Pandas · Scikit-Learn · Matplotlib · Seaborn**

---

# ⚙️ Task 3 — Model Optimization

## 🎯 Objective

Improve machine learning model performance using **Hyperparameter Tuning** and **Regularization**, then compare baseline models with their optimized versions.

## ⚙️ Approach

### 1. Baseline Models

Trained three models using their default hyperparameters:

* Logistic Regression
* Decision Tree
* Support Vector Machine (SVM)

The baseline results were used as a reference for measuring the impact of optimization.

### 2. Hyperparameter Tuning

Used **GridSearchCV** with **5-fold cross-validation** to systematically search for better hyperparameter combinations.

Parameters explored included:

* Logistic Regression → `C`
* Decision Tree → `criterion`, `max_depth`, `min_samples_split`
* SVM → `C`, `gamma`, `kernel`

### 3. Regularization Analysis

Investigated the effect of different `C` values on Logistic Regression.

Compared:

* Training accuracy
* Testing accuracy

This helped visualize the relationship between **underfitting, good generalization, and overfitting**.

### 4. Baseline vs Optimized Comparison

Evaluated the optimized models on the test dataset and compared their performance against the original baseline models.

### 5. Final Model Validation

Validated the best-performing optimized model using sample test cases.

## 🔍 Best Hyperparameters Found

| Model                   | Best Parameters                                                  |
| ----------------------- | ---------------------------------------------------------------- |
| **Logistic Regression** | `C = 10`                                                         |
| **Decision Tree**       | `criterion = entropy`, `max_depth = 5`, `min_samples_split = 10` |
| **SVM**                 | `C = 1`, `gamma = scale`, `kernel = rbf`                         |

## 💡 Key Learnings

This task helped me understand that:

* Default hyperparameters are not always optimal.
* Hyperparameter tuning can improve model performance and generalization.
* Cross-validation provides a more reliable way to select model parameters.
* Regularization helps control model complexity.
* Very low regularization strength can lead to underfitting, while excessive model flexibility can increase overfitting.
* Model optimization is an important step after establishing a baseline model.

### 🏆 Best Overall Model

After optimization, **SVM remained the strongest overall performer** with:

```text
C = 1
gamma = scale
kernel = rbf
```

## 📂 Task 3 Files

| File                             | Description                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `README.md`                      | Task documentation                                                                                               |
| `task3_model_optimization.ipynb` | Complete notebook covering baseline models, hyperparameter tuning, regularization analysis, and model comparison |

## 🛠️ Tools

**Python · Pandas · Scikit-Learn · GridSearchCV · Matplotlib · Seaborn**

---

# 🛠️ Tools & Technologies

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Machine Learning Techniques

* Data Cleaning
* Exploratory Data Analysis
* Feature Encoding
* Feature Scaling
* Binary Classification
* Logistic Regression
* Decision Trees
* Support Vector Machines
* Model Evaluation
* Hyperparameter Tuning
* GridSearchCV
* Cross-Validation
* Regularization

### Development & Version Control

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📂 Repository Structure

The following structure reflects the **actual organization of this repository**:

```text
skillsQuark-ml-internship/
│
├── Task1/
│   ├── README.md
│   ├── Task1_EDA_Preprocessing.py
│   ├── Task1_Report.txt
│   ├── cleaned_data.csv
│   ├── eda_visualization.png
│   └── output.csv
│
├── Task2/
│   ├── README.md
│   └── task2_supervised_models.ipynb
│
├── Task3/
│   ├── README.md
│   └── task3_model_optimization.ipynb
│
└── README.md
```

---

# 📈 Learning Progression

These tasks represent my progression through the core stages of a machine learning workflow:

```text
Data Understanding
       ↓
Data Cleaning & EDA
       ↓
Data Preprocessing
       ↓
Supervised Learning
       ↓
Model Evaluation
       ↓
Hyperparameter Tuning
       ↓
Regularization
       ↓
Model Optimization
```

Starting from raw data in **Task 1**, I progressed to building and comparing classification models in **Task 2**, and finally learned how to optimize those models through **hyperparameter tuning and regularization in Task 3**.

---

# 🎓 About This Repository

This repository documents my practical learning journey as a **Machine Learning Intern at SkillSquark**.

Rather than focusing only on theoretical concepts, these tasks provided hands-on experience with the complete machine learning workflow — from **understanding and preparing data to training, evaluating, and optimizing machine learning models**.

Each task helped me strengthen my Python, data analysis, and machine learning skills while developing a better understanding of how machine learning workflows are built in practice.

---

## 👤 Author

**Kiran Shehzadi**

Machine Learning Intern | BS Information Technology

---

⭐ *Learning by building, experimenting, and improving — one machine learning task at a time.*
