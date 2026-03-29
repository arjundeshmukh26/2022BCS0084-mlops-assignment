import pandas as pd

# Load dataset
df = pd.read_csv("data/winequality-red.csv")

# Create smaller dataset (50%)
df_small = df.sample(frac=0.5, random_state=42)

# Save it (overwrite same file)
df_small.to_csv("data/winequality-red.csv", index=False)

print("Small dataset created")
