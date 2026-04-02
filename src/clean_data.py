import pandas as pd

# Load dataset
df = pd.read_csv('data/sample_data.csv')

# Detect missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Fill missing numeric values with mean
df = df.fillna(df.mean(numeric_only=True))

# Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)

print("✅ Cleaned data saved to data/cleaned_data.csv")