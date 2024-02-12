import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"): # keys are mandatory for forms
    user_email = st.text_input("Your Email Adress")
    message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {message}

"""
    button = st.form_submit_button("Submit")
    if button: # a boolean type
        send_email(message)
        st.info("Email was successfully sent. we will get back to you asap")

# app password: jjbh sohi drrq tjko
