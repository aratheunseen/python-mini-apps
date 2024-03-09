import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Data Visualization Dashboard")

df = pd.read_csv("happy.csv")

enum = list(df.columns)

x = st.selectbox("Select the data for X-axis",
             (enum))
y = st.selectbox("Select the data for Y-axis",
             (enum))

st.subheader(f"{x} and {y}")

figure = px.scatter(x=df[f'{x.lower()}'],
                 y=df[f'{y.lower()}'],
                 labels={"x":x,"y":y})

st.plotly_chart(figure)