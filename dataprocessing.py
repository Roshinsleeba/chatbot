import pandas as pd

# Load the dataset
df = pd.read_csv("breastcancer.csv")



# Save cleaned data (optional)
df.to_csv("cleaned_dataset.csv", index=False)
print(df.isnull().sum())

