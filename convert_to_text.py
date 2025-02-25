import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Convert each row into a text-based document
text_data = []

for _, row in df.iterrows():
    text_entry = f"""
    Patient Information:
    - Age: {row['Age']}
    - Race: {row['Race']}
    - Marital Status: {row['Marital Status']}
    - Tumor Stage: {row['T Stage']}, {row['N Stage']}
    - 6th Stage: {row['6th Stage']}
    - Differentiation: {row['differentiate']}
    - Grade: {row['Grade']}
    - Tumor Size: {row['Tumor Size']}
    - Estrogen Status: {row['Estrogen Status']}
    - Progesterone Status: {row['Progesterone Status']}
    - Regional Nodes Examined: {row['Regional Node Examined']}
    - Regional Nodes Positive: {row['Reginol Node Positive']}
    - Survival Months: {row['Survival Months']}
    - Status: {row['Status']}
    """
    text_data.append(text_entry.strip())

# Save the text data into a file
with open("dataset_texts.txt", "w", encoding="utf-8") as f:
    for text in text_data:
        f.write(text + "\n\n")

print("Dataset converted to text and saved as 'dataset_texts.txt'.")
