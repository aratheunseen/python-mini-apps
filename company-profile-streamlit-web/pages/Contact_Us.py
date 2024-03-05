import streamlit as st
import pandas as pd
from contact_form import send_mail

df = pd.read_csv("topics.csv")

with st.form(key="contact"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",
                         options=df['topic'])
    message = st.text_area("Text")
    button = st.form_submit_button("Submit")

    if button:
        if email == "" or topic == "" or message == "":
            st.error("Please fill in all the fields.")
        else:
            send_mail(email,topic,message)
            st.success(f"Thank you for your message! We will get back to you at {email} as soon as possible.")
            st.stop()
    else:
        pass

st.info("© 2024 aratheunseen. All rights reserved.")