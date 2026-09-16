import pandas as pd


# Load the credit card fraud dataset
df = pd.read_csv("data/creditcard.csv")

# Display basic information
print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nClass distribution:")
print(df["Class"].value_counts())