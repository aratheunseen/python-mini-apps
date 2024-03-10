import streamlit as st
import glob
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

x_data = []
positivity = []
negativity = []

st.title("Sentiment Analysis Dashboard")

filepaths = sorted(glob.glob("diary/*.txt"))

for filepath in filepaths:
    x_data.append(filepath[6:-4])

    with open(filepath,"r") as file:
              content = file.read()

    score = analyzer.polarity_scores(content)

    positivity.append(score['pos'])
    negativity.append(score['neg'])


st.subheader("Positivity")
pos_figure = px.line(x=x_data,y=positivity,labels={"x":"Date","y":"Sentiment"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=x_data,y=negativity,labels={"x":"Date","y":"Sentiment"})
st.plotly_chart(neg_figure)