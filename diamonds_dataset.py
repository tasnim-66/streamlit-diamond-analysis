import seaborn as sns
import pandas as pd

# Load dataset
diamonds = sns.load_dataset("diamonds")

# Select a subset of the dataset (to avoid too much data)
subset_diamonds = diamonds.sample(500)  # Pick 500 random rows

# Save to CSV (for easy copy-paste into Google Sheets)
subset_diamonds.to_csv("diamonds_subset.csv", index=False)

print("Saved 'diamonds_subset.csv'. Open it and copy the content into Google Sheets.")
