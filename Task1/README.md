Task 1: EDA & Preprocessing — Titanic Dataset
Objective

Perform a comprehensive Exploratory Data Analysis (EDA) on the Titanic dataset and prepare it for modeling — handling missing values, encoding categorical features, and treating outliers using Pandas.
Approach

    Data Inspection — Reviewed dataset shape, data types, and summary statistics.
    Missing Value Analysis — Visualized and quantified nulls; found major gaps in Age (~20%) and Cabin (~77%).
    Univariate & Bivariate Analysis — Explored feature distributions and relationships (correlation heatmap, boxplots vs. Survived).
    Data Cleaning
        Imputed Age with median, Embarked with mode
        Dropped Cabin (excessive missingness)
        Removed non-predictive identifiers: Name, Ticket, PassengerId
        Checked and removed true duplicate records
    Feature Encoding
        Sex → binary numeric
        Embarked → one-hot encoded
    Outlier Treatment — Capped Fare outliers using the IQR method.
    Validation & Export — Confirmed a null-free, fully numeric dataset and exported it.

Key Insights

    Cabin was too sparse to impute meaningfully and was dropped.
    Fare and Pclass show a notable negative correlation.
    Age distribution is similar across survivors and non-survivors — not a strong standalone predictor.

Files in This Folder
File 	Description
eda.ipynb 	Full analysis notebook with step-by-step markdown documentation
train.csv 	Raw, unprocessed dataset (891 rows, 12 columns)
clean_data.csv 	Final cleaned, encoded, model-ready dataset
Tools Used

Python · Pandas · NumPy · Matplotlib · Seaborn
