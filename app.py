import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

diamonds = sns.load_dataset('diamonds')
st.title("Diamond price analysis: A/B Testing")

st.write("Preview of the Diamonds Dataset:")
st.dataframe(diamonds.head())  

# Business Question
st.subheader("What are the factors that influence the price of a diamond the most?")

st.write(
    "This app compares two different visualizations: \n"
    "- A **boxplot** to compare prices across different cut categories\n"
    "- A **line chart** to show the relationship between carat size and price"
)

# Function 1: Boxplot (Cut vs. Price)
def plot_boxplot():
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=diamonds, x="cut", y="price", palette="pastel", width=0.6, showfliers=False, ax=ax)
    ax.set_title("💎 Diamond Price by Cut Quality", fontsize=16, fontweight="bold")
    ax.set_xlabel("Cut Quality", fontsize=14)
    ax.set_ylabel("Price ($)", fontsize=14)
    st.pyplot(fig)

# Function 2: Line Chart (Carat vs. Price)
def plot_linechart():
    fig, ax = plt.subplots(figsize=(12, 6))
    diamonds_sorted = diamonds.sort_values("carat")
    diamonds_sorted["rolling_price"] = diamonds_sorted["price"].rolling(50).median()

    sns.lineplot(data=diamonds_sorted, x="carat", y="rolling_price", color="blue", linewidth=2, ax=ax)
    ax.set_title("📈 How Carat Size Affects Diamond Price", fontsize=16, fontweight="bold")
    ax.set_xlabel("Carat Size", fontsize=14)
    ax.set_ylabel("Median Price ($)", fontsize=14)
    st.pyplot(fig)

# User Interaction in Streamlit
st.write("## Choose a visualization to display:")

# Add a radio button to select a plot
chart_option = st.radio("Select a chart:", ["Boxplot - Cut vs Price", "Line Chart - Carat vs Price"])

# Show the selected chart
if chart_option == "Boxplot - Cut vs Price":
    plot_boxplot()
else:
    plot_linechart()

