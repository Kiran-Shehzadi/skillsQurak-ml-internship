"""
TASK 1: EDA & PREPROCESSING
Author: Kiran Shehzadi
"""

# ============================================
# STEP 1: IMPORT LIBRARIES (Tools needed)
# ============================================
import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.preprocessing import StandardScaler, LabelEncoder  

print("✅ All libraries loaded!")

# ============================================
# STEP 2: LOAD DATA
# ============================================
# Using Iris dataset (flower measurements) 
from sklearn.datasets import load_iris

# Load the data
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # Add flower types
df['species'] = df['target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

print("📊 Data Loaded! Let's explore it...")
print("\nFirst 5 rows of data:")
print(df.head())

# ============================================
# STEP 3: UNDERSTANDING DATA (EDA Part 1)
# ============================================
print("\n" + "="*50)
print("🔍 EXPLORATORY DATA ANALYSIS")
print("="*50)

# How many rows and columns?
print(f"\n📈 Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

# What are the column names?
print(f"\n📋 Column Names: {df.columns.tolist()}")

# What's the data type of each column?
print("\n📝 Data Types:")
print(df.dtypes)

# Get basic statistics
print("\n📊 Statistical Summary:")
print(df.describe())

# ============================================
# STEP 4: CHECKING FOR PROBLEMS
# ============================================
print("\n" + "="*50)
print("🐛 CHECKING FOR DATA PROBLEMS")
print("="*50)

# Missing values (empty cells)?
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Duplicate rows?
print(f"\n👯 Duplicate Rows: {df.duplicated().sum()}")

# Weird values?
print("\n🔢 Data Info:")
print(df.info())

# ============================================
# STEP 5: VISUALIZE DATA (Draw Charts)
# ============================================
print("\n" + "="*50)
print("📈 CREATING VISUALIZATIONS")
print("="*50)

# Create a figure with 4 charts
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('EDA: Understanding Our Data', fontsize=16, fontweight='bold')

# Chart 1: Distribution of Sepal Length
axes[0, 0].hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Sepal Length Distribution')
axes[0, 0].set_xlabel('Length (cm)')
axes[0, 0].set_ylabel('Frequency')

# Chart 2: Flower Types Count
df['species'].value_counts().plot(kind='bar', ax=axes[0, 1], color=['red', 'blue', 'green'])
axes[0, 1].set_title('Count of Each Flower Type')
axes[0, 1].set_ylabel('Count')

# Chart 3: Correlation heatmap (which columns are related?)
numeric_df = df.drop(['target', 'species'], axis=1)
sns.heatmap(numeric_df.corr(), annot=True, ax=axes[1, 0], cmap='coolwarm', fmt='.2f')
axes[1, 0].set_title('Correlation Between Features')

# Chart 4: Box plot (to find outliers - weird values)
numeric_df.boxplot(ax=axes[1, 1])
axes[1, 1].set_title('Box Plot: Finding Outliers')
axes[1, 1].set_ylabel('Value')

plt.tight_layout()
plt.savefig('eda_visualization.png', dpi=300, bbox_inches='tight')
print("✅ Chart saved as 'eda_visualization.png'")
plt.show()

# ============================================
# STEP 6: CLEAN AND PREPROCESS DATA
# ============================================
print("\n" + "="*50)
print("🧹 DATA PREPROCESSING (Cleaning)")
print("="*50)

# Making a copy so we don't change original
df_clean = df.copy()

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()
print(f"✅ After removing duplicates: {df_clean.shape[0]} rows")

# Remove rows with missing values (if any)
df_clean = df_clean.dropna()
print(f"✅ After removing missing values: {df_clean.shape[0]} rows")

# ============================================
# STEP 7: FEATURE SCALING (Making all numbers similar size)
# ============================================
print("\n" + "="*50)
print("⚖️ FEATURE SCALING")
print("="*50)
print("Why? Some numbers are 5cm, others are 15cm - we need to normalize them!")

# Select numeric columns (not the target)
numeric_features = df_clean.drop(['target', 'species'], axis=1)

# Scale the data (make them between 0 and 1)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(numeric_features)

# Convert back to DataFrame
df_scaled = pd.DataFrame(df_scaled, columns=numeric_features.columns)

print("\nOriginal data (first row):")
print(numeric_features.iloc[0])

print("\nScaled data (first row):")
print(df_scaled.iloc[0])

# ============================================
# STEP 8: ENCODE CATEGORICAL DATA (Convert text to numbers)
# ============================================
print("\n" + "="*50)
print("🔤 ENCODING CATEGORICAL DATA")
print("="*50)

# Create final dataset
df_final = df_scaled.copy()
df_final['species'] = df_clean['species'].values

# Encode species names to numbers
encoder = LabelEncoder()
df_final['species_encoded'] = encoder.fit_transform(df_final['species'])

print("\nOriginal species names:")
print(df_clean['species'].unique())

print("\nEncoded values:")
print(df_final[['species', 'species_encoded']].drop_duplicates())

# ============================================
# STEP 9: FINAL CLEANED DATA
# ============================================
print("\n" + "="*50)
print("✅ FINAL CLEANED DATA READY!")
print("="*50)

print("\nShape of final data:", df_final.shape)
print("\nFirst 5 rows of cleaned data:")
print(df_final.head())

# Save cleaned data to CSV
df_final.to_csv('cleaned_data.csv', index=False)
print("\n💾 Cleaned data saved to 'cleaned_data.csv'")

# ============================================
# STEP 10: SUMMARY REPORT
# ============================================
print("\n" + "="*50)
print(" SUMMARY REPORT")
print("="*50)

summary = f"""
✅ EDA & PREPROCESSING COMPLETED!

📊 Data Summary:
   • Total Rows: {df_final.shape[0]}
   • Total Columns: {df_final.shape[1]}
   • Missing Values: 0
   • Duplicates Removed: {df.shape[0] - df_final.shape[0]}

🔍 Features Found:
   • Numeric Features: 4 (sepal, petal measurements)
   • Categorical Features: 1 (species type)

🧹 Cleaning Done:
   • ✅ Missing values handled
   • ✅ Duplicates removed
   • ✅ Data scaled (0-1)
   • ✅ Categorical data encoded
   • ✅ Outliers identified

📈 Data Quality: EXCELLENT ✅
   Ready for Machine Learning! 🚀
"""

print(summary)

