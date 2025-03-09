import seaborn as sns
import streamlit as st


tab1, tab2 = st.tabs(["Tab1", "Tab2"])
with tab1:
    st.write("This is tab 1")

    iris = sns.load_dataset("iris")
    fig = plt.figure()
    st.pyplot(fig)
    chart= sns.barplot(x="species", y="sepal_length", data=iris)

with tab2:
    st.write("This is tab 2")
