import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# For this activity I will use the diamonds dataset from seaborn
diamonds = sns.load_dataset('diamonds')
print(diamonds.head()) # to discover the data 
print(diamonds.columns)


# Add these lines to handle SSL verification
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

# Business Question considering this diamond dataset: What are the factors that influence the most the price of a diamond?
# For the A/B Testing I will create two different charts: A boxplot to compare prices accross different cut categories and a line chart to show the relationship between carat size and price. 

# 1. BOX PLOT: "Does cut quality affect price?"
plt.figure(figsize=(12, 6))
sns.boxplot(data =diamonds, x ="cut", y ="price", palette ="pastel", width =0.6, showfliers =False)
plt.title("Diamond price by Cut quality", fontsize =16, fontweight ="bold")
plt.xlabel("Cut quality", fontsize =14)
plt.ylabel("Price", fontsize =14)
plt.xticks(fontsize =12)
plt.yticks(fontsize =12)
plt.show()


# 2. Line Chart - Median Price by Carat
plt.figure(figsize =(12, 6))
diamonds_sorted = diamonds.sort_values("carat")
diamonds_sorted["rolling_price"] = diamonds_sorted["price"].rolling(50).median()
sns.lineplot(data =diamonds_sorted, x ="carat", y ="rolling_price", color ="blue", linewidth =2)
plt.title("How Carat size affects diamond price", fontsize=16, fontweight="bold")
plt.xlabel("Carat Size", fontsize=14)
plt.ylabel("Median Price", fontsize=14)
#plt.annotate("Price jumps after 2 carats", xy=(2, 8000), xytext=(2.5, 12000), arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color="red")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

