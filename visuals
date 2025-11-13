# app.py
# Streamlit app visualizing Dr. Ignaz Semmelweis’s handwashing data
# code snippet assisted by ChatGPT

import streamlit as st
import pandas as pd
import altair as alt

st.title("Dr. Ignaz Semmelweis and the Discovery of Handwashing 🧼")
st.write("""
In the mid-1800s, Dr. Ignaz Semmelweis discovered that handwashing dramatically reduced deaths in maternity clinics.
This dataset compares the number of births and deaths before and after the introduction of handwashing.
""")

df = pd.read_csv("yearly_deaths_by_clinic-1.csv")

st.subheader("Raw Data Preview")
st.dataframe(df)

df["death_rate"] = df["deaths"] / df["births"]

st.subheader("Death Rate by Year and Clinic")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="year:O",
    y=alt.Y("death_rate:Q", title="Death Rate"),
    color="clinic:N"
).properties(width=700, height=400)

st.altair_chart(chart)

st.markdown("""
### 🩺 Findings
After 1847, when **handwashing** was introduced at Clinic 1, the **mortality rate dropped dramatically**.
This visual evidence supports Semmelweis’s conclusion that cleanliness saves lives.
""")
