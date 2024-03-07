import streamlit as st
import requests

date = "2024-03-04"
api_key = "DEMO_KEY"
response = requests.get(f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}")

content = response.json()

local_image_path = f"photos/{date}.jpeg"
local_response = requests.get(content['url'])
with open(local_image_path,"wb") as file:
    file.write(local_response.content)

st.title(content['title'])
st.write("Copyright: " + content['copyright'])
st.image(local_image_path)
st.write(content['explanation'])
