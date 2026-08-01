import streamlit as st
import pandas as pd

st.title(" Coffee Sales Dashboard")

file = st.file_uploader("Upload your Coffee CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader(" Data Preview")
    st.dataframe(df)

    st.subheader(" Summary Statistics")
    st.write(df.describe())

    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by City", cities)

    filtered_data = df[df["City"] == selected_city]

    st.subheader(f" Coffee Sales in {selected_city}")
    st.dataframe(filtered_data)