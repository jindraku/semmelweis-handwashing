import streamlit as st
import pandas as pd
import altair as alt

st.title("Dr. Semmelweis and the Birth of Hand Hygiene")
st.write("""
In the mid-1800s, Dr. Ignaz Semmelweis discovered that handwashing dramatically reduced deaths in maternity clinics.
This dataset compares the number of births and deaths before and after the introduction of handwashing.
""")

df = pd.read_csv("yearly_deaths_by_clinic-1.csv")

st.subheader("Data at a Glance")
st.dataframe(df)

# Use correct column names from the CSV
df["death_rate"] = df["Deaths"] / df["Birth"]

st.subheader("Proof in the Data: Handwashing Saves Lives")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Year:O",
    y=alt.Y("death_rate:Q", title="Death Rate"),
    color="Clinic:N"
).properties(width=700, height=400)

st.altair_chart(chart)

st.markdown("""
### 🩺 Findings
After 1847, when handwashing was formally introduced in Clinic 1, the clinic experienced a sharp and unprecedented decline in mortality rates. 
The pattern in the data provides clear, quantitative evidence that improved hygiene practices, specifically 
handwashing, were directly associated with saving lives, reinforcing Semmelweis’s groundbreaking conclusion about the importance of cleanliness in medical care.
""")
