import pandas as pd

# Load dataset
df = pd.read_csv('data/Telugu_songs.csv')

# Preview basic info
print("✅ Dataset loaded successfully!\n")
print("📊 Shape of the dataset:", df.shape)
print("\n🧩 Column names:\n", df.columns.tolist())
print("\n🔍 Checking for missing values:\n", df.isnull().sum())

# Show first few rows
print("\n👀 Preview of data:\n", df.head())
