import os
import streamlit as st
import numpy as np
from PIL import Image

# Custom imports
from app import MultiPage
from pages import monkeypox

# Create an instance of the app
app = MultiPage()
st.header("AI-DRIVEN SKIN DISEASE CLASSIFICATION: A DEEP LEARNING APPROACH FOR EARLY DETECTION")
# Section 00 - Our Mission
st.header("Our Mission")
st.write(
    "Creating a deep learning model for the detection and classification of diseases like monkeypox, chickenpox, measles, and normal skin conditions in images is a valuable application in the healthcare domain. To promote research in the field of Health Care. "
    "In order to improve the efficiency of Health Care delivery Systems. To promote the development of high-quality hospital services and community health care."
)

# Title of the main page
st.title("HEALTH CARE INFO")
monkeypox_image_url = "https://static.toiimg.com/photo/93497702.cms"
chickenpox_image_url = "https://img.etimg.com/thumb/msid-103654226,width-640,height-480,imgsize-1374192,resizemode-4/what-is-it.jpg"
measles_image_url = "https://health.uct.ac.za/sites/default/files/styles/standard_med/public/content_migration/health_uct_ac_za/1457/images/Measles%25202.001_0.jpeg?h=fbf7a813&itok=zXtJNDmo"

# Section 1 - Monkeypox Information
st.header("Monkeypox")

# Create a two-column layout using st.columns()
col1, col2 = st.columns(2)

# Display the Monkeypox image in the second column
with col2:
    st.image(monkeypox_image_url, use_column_width=True)

# Display Monkeypox text in the first column
with col1:
    st.write(
        "Monkeypox is a rare, zoonotic viral disease that typically causes fever, rash, and painful lesions in humans. "
        "Though milder than smallpox, severe cases can occur. It's transmitted through animals, particularly rodents, "
        "and human-to-human contact."
    )
    if st.button("Know more about Monkeypox", key="monkeypox"):
        st.write("[Learn more about Monkeypox](https://www.who.int/news-room/fact-sheets/detail/monkeypox)")

# Section 2 - ChickenPox Information (You can repeat the same layout structure for other sections)
st.header("ChickenPox")

# Create a two-column layout using st.columns()
col1, col2 = st.columns(2)

# Display the ChickenPox image in the second column
with col1:
    st.image(chickenpox_image_url, use_column_width=True)

# Display ChickenPox text in the first column
with col2:
    st.write(
        "Chickenpox, caused by the varicella-zoster virus, presents with a characteristic itchy rash, fever, and flu-like symptoms. "
        "It's highly contagious through respiratory droplets and can lead to complications, especially in adults and the immunocompromised."
    )
    if st.button("Know more about ChickenPox", key="chickenpox"):
        st.write("[Learn more about ChickenPox](https://www.cdc.gov/chickenpox/index.html)")

# Section 3 - Measles Information (Repeat the same layout structure for other sections)
st.header("Measles")

# Create a two-column layout using st.columns()
col1, col2 = st.columns(2)

# Display the Measles image in the second column
with col2:
    st.image(measles_image_url, use_column_width=True)

# Display Measles text in the first column
with col1:
    st.write(
        "Measles is a highly contagious viral illness, caused by the measles virus. It features fever, cough, and a distinctive red rash. "
        "Measles can result in severe complications, including pneumonia and encephalitis. Vaccination is crucial for prevention and global control."
    )
    if st.button("Know more about Measles", key="measles"):
        st.write("[Learn more about Measles](https://www.who.int/india/health-topics/measles)")
        
import pandas as pd
# Create a dictionary with the symptoms of each disease
st.header("********SYMPTOMS OF SIMILAR SKIN DISEASES********")
symptoms = {
    "Monkeypox": [
        "Fever",
        "Rash",
        "Painful lesions",
        "Swelling of lymph nodes",
        "Muscle aches",
        "Chills",
    ],
    "Chickenpox": [
        "Itchy rash",
        "Fever",
        "Headache",
        "Fatigue",
        "Loss of appetite",
        "Fluid-filled blisters",
    ],
    "Measles": [
        "High fever",
        "Cough",
        "Runny nose",
        "Red, watery eyes",
        "Koplik spots",
        "Rash",
    ],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(symptoms)

# Display the table
st.table(df)

# Add all your application here
app.add_page("Monkeypox Or Not", monkeypox.app)
# The main app
app.run()



# Dropdown for Location
st.markdown("\U0001F468‍⚕️ \U0001F3E2 Want to know doctors who are nearby?\U0001F468‍⚕️ \U0001F3E2")
location = st.selectbox("Enter your location:", ["Select your location"] + [
    "Hyderabad", "Warangal", "Karimnagar", "Adilabad", "Komram Bheem", "Bhadradri",
    "Jayashankar", "Gadwal", "Jagtial", "Jangaon", "Kamareddy", "Khammam",
    "Mahabubabad", "Mahbubnagar", "Mancherial", "Medak", "Medchal", "Nalgonda",
    "Nagarkurnool", "Nirmal", "Nizamabad", "Ranga Reddy", "Rajanna", "Sangareddy",
    "Siddipet", "Suryapet", "Vikarabad", "Wanaparthy", "Yadadri"
])

# Search Button
if st.button("Search"):
    if location == "Select your location":
        st.warning("Please select a location.")
    else:
        # Define Google Maps URLs for different locations
        location_urls = {
            "Hyderabad": "https://www.practo.com/hyderabad/treatment-for-skin-infections",
            "Warangal": "https://www.practo.com/warangal/doctor-for-skin-allergies",
            # Add URLs for other locations
        }

        # Redirect to the appropriate URL based on the selected location
        if location in location_urls:
            st.success(f"Redirecting to {location} monkeypox hospitals on Google Maps...")
            st.markdown(f"[Click here to view {location} hospitals]({location_urls[location]})")
import streamlit as st
import webbrowser

st.markdown("\U0001F914 \U0001F914 \U0001F914.Have any Questions?\U0001F914 \U0001F914 \U0001F914")
st.markdown("We have provided the Frequently Answered Questions, click on the below button")

# Function to open the FAQ website in a new tab
def open_faq_page():
    webbrowser.open("https://2003a52127.github.io/monkeypox_blog/faq.html")

# Create a button in the top-right corner
if st.button("FAQ", key="faq_button", help="Click to view FAQ"):
    open_faq_page()
