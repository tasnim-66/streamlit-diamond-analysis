import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time

# Load the dataset
st.set_page_config(page_title="Diamond Price Analysis", layout="wide")

# Title and introduction
st.title("Diamond Price Analysis: A/B Testing")
st.write(
    "Welcome! This app explores the factors that influence the price of a diamond. "
    "You will see one of two different visualizations at random and compare their effectiveness."
)

# Display dataset preview
st.subheader("Preview of the Diamonds Dataset")
diamonds = sns.load_dataset("diamonds")
st.dataframe(diamonds.head())

# Business question prominently displayed
st.header("Which Factor Influences Diamond Prices the Most?")
st.subheader("Does cut quality or carat size have a bigger impact on diamond price?")

# Function 1: Boxplot (Cut vs. Price)
def plot_boxplot():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=diamonds, x="cut", y="price", palette="Set2", width=0.6, showfliers=False, ax=ax)
    ax.set_title("Diamond Price by Cut Quality", fontsize=14, fontweight="bold")
    ax.set_xlabel("Cut Quality", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)  # Removed "$" symbol
    st.pyplot(fig)

# Function 2: Line Chart (Carat vs. Median Price)
def plot_linechart():
    fig, ax = plt.subplots(figsize=(10, 6))
    diamonds_sorted = diamonds.sort_values("carat")
    diamonds_sorted["rolling_price"] = diamonds_sorted["price"].rolling(50).median()

    sns.lineplot(data=diamonds_sorted, x="carat", y="rolling_price", color="blue", linewidth=2, ax=ax)
    ax.set_title("How Carat Size Affects Diamond Price", fontsize=14, fontweight="bold")
    ax.set_xlabel("Carat Size", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)  # Removed "$" symbol

    # Highlight the price jump
    ax.annotate("Significant Price Increase After 2 Carats", xy=(2, 8000), xytext=(2.5, 12000),
                arrowprops=dict(facecolor='red', shrink=0.05),
                fontsize=12, color="red")

    st.pyplot(fig)

# **A/B Testing Mechanism (Ensuring Random Selection and Timing)**
if "chart_selected" not in st.session_state:
    st.session_state.chart_selected = None
    st.session_state.start_time = None
    st.session_state.show_second_button = False

# **First Button: Randomly Selects a Chart**
if st.button("Show a Random Chart"):
    st.session_state.chart_selected = random.choice(["boxplot", "linechart"])
    st.session_state.start_time = time.time()  # Start the timer
    st.session_state.show_second_button = True  # Enable second button

# **Display the randomly selected chart**
if st.session_state.chart_selected:
    if st.session_state.chart_selected == "boxplot":
        plot_boxplot()
    else:
        plot_linechart()

    # **Second Button: Measures the response time**
    if st.session_state.show_second_button:
        if st.button("I Answered the Question"):
            response_time = time.time() - st.session_state.start_time
            st.success(f"Great job! You answered in {round(response_time, 2)} seconds.")

# **Conclusion Section**
st.subheader("Insights & Key Takeaways")
st.write(
    "- **Cut Quality:** Cut quality has a moderate impact on price. "
    "Premium cuts tend to be slightly higher priced, but it is not the dominant factor.\n"
    "- **Carat Size:** Prices increase significantly after 2 carats, indicating a threshold where "
    "diamonds become much more expensive.\n"
    "- **Overall Conclusion:** While both factors matter, carat size plays the biggest role in determining price."
)

