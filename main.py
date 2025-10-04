import streamlit as st
import pandas as pd

st.title("Nairisz's Resume")

st.subheader("Norizzaty Binti Norsupardi")

st.header("Contact Information")
st.write("Email: norizzaty.norsupard@gmail.com")
st.write("Phone: (60) 19-223 8570")
st.write("LinkedIn: linkedin.com/in/norizzaty-norsupardi")

st.header("Education")

edu = pd.DataFrame({
    "Degree": ["Diploma", "Degree"],
    "Institution": ["Kolej Vokasional Kuala Krai", "Universiti Malaysia Kelantan"],
    "Field": ["Multimedia Creative Animation", "Bachelor of Information Technology (Hons) (AI track)"],
    "Year": [2016, 2022]
})
st.write(edu)

st.header("Work Experience")

exp = pd.DataFrame({
    "Job Title": ["Internship", "Contract", "Part-Time"],
    "Company": ["Talentiv", "Talentiv", "Tealive"],
    "Year": ["Jan 2020 - Mar 2020", "Jul 2020 - Jun 2021", "Apr 2022 - Oct 2022"],
    "Description": [
        "Support on-site production and deliver post-production editing for dramas and television programmes.",
        "Edited dramas and TV programmes, and supported production with equipment handling and proposal drafting.",
        "Provided excellent customer service and food handling."
    ]
})
st.write(exp)

st.header("Achievements")
st.write("- Involved in editing drama for TV3 and RTM (2020-2021).")
st.write("- Involved in editing TV programme for RTM and JAKIM during internship (2020).")
st.write("- Won 1st place in Traiblazer Cup Competition @ FSDK (2025).")
st.write("- Won Best Business Model in Trailblazer Competition @ FSDK (2025).")
st.write("- Achieved Dean's List for 3 semesters.")

st.header("Skills")
st.write("- Video Editing")
st.write("- Customer Service")
st.write("- Digital Illustration")
st.write("- UI/UX Design")

st.header("Projects")
proj = pd.DataFrame({
    "Project Name": ["Pet Grooming Service", "Student Supervision Management System", "Library Management System", 
                     "Bus Schedule App", "Smart Crosswalk", "VendiMed", "The Healthcare Disease Prediction for Diabetes", 
                     "Regression For Flood Forecasting: Case Study in Gong Kedak, Terengganu", "Analysis Movie Rating",
                     "FBMKLCI Stock Price Prediction using LSTM", 
                     "Predicting the Risk of Heart Disease using Multiple Machine Learning Algorithms"],
    "Year": [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    "Description": [
        "Developing a booking system for pet grooming services using Python.",
        "Creating an application for student management (tracking class, attendance, and performance) and database for it.",
        "Developing a library management system with authentication, borrowing, and returning features and inventory updates using Java.",
        "Designing a bus schedule app with real-time updates and reminder using Flutter and Dart.",
        "Creating an IoT project for smart crosswalk system with sensors to detect pedestrian and traffic light control.",
        "Developing a vending machine prototype that dispense medications while integrated with app for booking and pick up scheduled medicines.",
        "Creating a healthcare disease prediction system focusing on diabetes using Fuzzy Logic with several combination of SVM, RF and LSTM.",
        "Building a flood forecasting system focusing on Gong Kedak, Terengganu using regression analysis.",
        "Analyzing movie ratings using Hadoop and MapReduce to find patterns and trends.",
        "Predicting stock prices using LSTM neural networks and find the best tuning parameters.",
        "Developing a heart disease risk prediction model using several ML and compare the accuracy results."
    ]
})
st.write(proj)

st.header("Activities")
st.write("- Participated in PEWARIS KPT Siri 1 (2023).")
st.write("- Joined the university's PRS (Pembimbing Rakan Siswa) club (2023/2024).")
st.write("- Joined for PRS Exco Publicity (2023/2024).")

st.header("References")
st.write("Name: Prof. Madya Ts. Dr. Hasyiya Karimah Binti Adli")
st.write("Email: hasyiya@umk.edu.my")
st.write("Phone: (60) 18-337 9687")
