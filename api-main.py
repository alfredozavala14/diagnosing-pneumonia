import streamlit as st
from PIL import Image
import numpy as np
from datetime import date
from src.helpers import check_email
from src.pdf_creator import create_PDF
from src.email import send_diagnosis_mail

image = Image.open("images/doctor-with-xray.jpg")
st.image(image)

st.write("""
# Automating Pneumonia Diagnosis
We are here to support you in diagnosing Pneumonia through x-rays.
Fill in the information below, upload the x-ray image in "jpeg", "jpg"
or "png" format and receive your diagnosis!
"""
)

# Insert patient's full name
full_name = st.text_input('Full Name')
if full_name:
    st.write('Hello ', full_name)

# Insert patient's email
email = st.text_input('Email')
if email and check_email(email) is False:
    st.error("Invalid email format")
elif email:
    st.write('Valid email')

# Insert x-ray date
d = st.date_input(
    "When was the x-ray taken?",
    value=date.today(),
    max_value=date.today()
)
st.write('The x-ray was taken on:', d)

# Upload x-ray image
uploaded_file = st.file_uploader("Choose a file to upload x-ray", type=['jpeg', 'jpg', 'png'])
if uploaded_file:
    st.write('File successfully uploaded')
    img = Image.open(uploaded_file)
    st.image(img)

# submit button
if st.button('Submit'):
    img_path = f"images/client_xrays/{full_name} xray - {d}.jpeg"
    img = img.save(img_path)
    create_PDF(
        patient_name = full_name,
        patient_email = email,
        xray_date = d,
        xray_path = img_path
    )
    send_diagnosis_mail(
        patient_name = full_name,
        patient_email = email
    )
    st.write('Diagnosis complete. Check your email for your results.')

