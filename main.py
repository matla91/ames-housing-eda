import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:/Users/HP/Documents/IA/Kaggle/ames-housing-eda/ames-housing-eda/data/archive/AmesHousing.csv")

# Display first rows
print(df.head())

# Count missing values in each column
missing_values = df.isnull().sum()

# Select only columns with missing values
missing_values = missing_values[missing_values > 0].sort_values(ascending=False)

# Display missing values
print(missing_values)

# Plot missing values
plt.figure(figsize=(12, 6))
plt.bar(missing_values.index, missing_values.values, color='royalblue')
plt.xticks(rotation=90)
plt.title("Number of Missing Values per Column")
plt.ylabel("Missing Values")
plt.xlabel("Columns")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()