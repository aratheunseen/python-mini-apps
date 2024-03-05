import streamlit as st
import pandas as pd

st.set_page_config("The Best Company")

st.title("The Best Company")
st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.\
            Donec auctor, nunc nec lacici tincidunt nunc,\
            nec tincidunt nunc odio c tincidunt\
            nunc odio tincidunt nunc, nec tincidunt nunc odio\
            tincidunt nunc,\
            nec tincidunt nunc odio tincidunt nunc, nec tincidunt\
            nunc odio tincidunt nunc nunc odio\
            tincidunt nunc, nec tincidunt.")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

def member_model(first_name,last_name,role,image):
    st.subheader(f"{first_name.capitalize()} {last_name.capitalize()}")
    st.write(role)
    st.image(f"images/{image}")

for i in range(3):
    for j in range(1):
        with col1:
            member_model(df.iloc[i,j],df.iloc[i,j+1],df.iloc[i,j+2],df.iloc[i,j+3])
        with col2:
            member_model(df.iloc[i+4,j],df.iloc[i+4,j+1],df.iloc[i+4,j+2],df.iloc[i+4,j+3])
        with col3:
            member_model(df.iloc[i+8,j],df.iloc[i+8,j+1],df.iloc[i+8,j+2],df.iloc[i+8,j+3])
        
st.info("© 2024 aratheunseen. All rights reserved.")