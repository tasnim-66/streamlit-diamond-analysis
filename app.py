import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time

# Load the dataset from Google Sheets
st.set_page_config(page_title="Diamond Price Analysis", layout="wide")

# Title and introduction
st.title("Diamond Price Analysis: A/B Testing")
st.write(
    "Welcome! This app explores the factors that influence the price of a diamond. "
    "You will see two different visualizations and compare their effectiveness."
)

# Display dataset preview
st.subheader("Preview of the Diamonds Dataset")
diamonds = sns.load_dataset("diamonds")
st.dataframe(diamonds.head())

# Ask for user input (optional - to personalize the experience)
user_name = st.text_input("Enter your name:", value="")

# Business question
st.subheader("Key Factors Affecting Diamond Price")
st.write(
    "- Carat Size: Does increasing carat size significantly impact price?\n"
    "- Cut Quality: Do higher quality cuts result in higher prices?"
)

# Function 1: Boxplot (Cut vs. Price)
def plot_boxplot():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=diamonds, x="cut", y="price", palette="Set2", width=0.6, showfliers=False, ax=ax)
    ax.set_title("Diamond Price by Cut Quality", fontsize=14, fontweight="bold")
    ax.set_xlabel("Cut Quality", fontsize=12)
    ax.set_ylabel("Price ($)", fontsize=12)
    st.pyplot(fig)

# Function 2: Line Chart (Carat vs. Median Price)
def plot_linechart():
    fig, ax = plt.subplots(figsize=(10, 6))
    diamonds_sorted = diamonds.sort_values("carat")
    diamonds_sorted["rolling_price"] = diamonds_sorted["price"].rolling(50).median()

    sns.lineplot(data=diamonds_sorted, x="carat", y="rolling_price", color="blue", linewidth=2, ax=ax)
    ax.set_title("How Carat Size Affects Diamond Price", fontsize=14, fontweight="bold")
    ax.set_xlabel("Carat Size", fontsize=12)
    ax.set_ylabel("Median Price ($)", fontsize=12)

    # Highlight the price jump
    ax.annotate("Significant Price Increase After 2 Carats", xy=(2, 8000), xytext=(2.5, 12000),
                arrowprops=dict(facecolor='red', shrink=0.05),
                fontsize=12, color="red")

    st.pyplot(fig)

# Timer Mechanism for A/B Testing
if "chart_selected" not in st.session_state:
    st.session_state.chart_selected = None
    st.session_state.start_time = None
    st.session_state.show_second_button = False

st.subheader("Choose a Visualization to Display")
chart_selection = st.radio("Select a chart:", ["Boxplot - Cut vs Price", "Line Chart - Carat vs Price"])

if st.button("Show Chart"):
    st.session_state.chart_selected = chart_selection
    st.session_state.start_time = time.time()  # Start timer

# Display the selected chart
if st.session_state.chart_selected:
    if st.session_state.chart_selected == "Boxplot - Cut vs Price":
        plot_boxplot()
    else:
        plot_linechart()

    # Show a second button to measure response time
    if st.button("I Found the Answer"):
        response_time = time.time() - st.session_state.start_time
        st.success(f"Great job, {user_name}! You answered in {round(response_time, 2)} seconds.")

# Conclusion Section
st.subheader("Insights & Key Takeaways")
st.write(
    "- Cut Quality: Cut quality has a moderate impact on price. "
    "Premium cuts tend to be slightly higher priced, but it is not the dominant factor.\n"
    "- Carat Size: Prices increase significantly after 2 carats, indicating a threshold where "
    "diamonds become much more expensive.\n"
    "- Overall: While both factors matter, carat size plays the biggest role in determining price."
)

st.write("Which visualization helped you understand this better? Let us know.")



