import streamlit as st
from Contact_Form import send_email

st.title("Contact Us")

with st.form(key='form',clear_on_submit=True,border=True):
    name = st.text_input("Your Name")
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    button = st.form_submit_button("Submit",use_container_width=True)

    if button:
        if name == '' or user_email == '' or message == '':
            st.error("Please fill in all the fields.")
        else:
            send_email(name,user_email,message)
            st.success(f"Thank you for your message! We will get back to you at {user_email} as soon as possible.")
            st.stop()
    else:
        pass

st.info("© 2024 aratheunseen. All rights reserved.")