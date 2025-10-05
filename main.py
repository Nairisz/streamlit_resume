import streamlit as st
import pandas as pd

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #645799;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


st.title("Norizzaty's Resume")

col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://github.com/Nairisz/streamlit_resume/raw/main/muka%20saya.jpg", width=160)

with col2:
    st.markdown("### Norizzaty Binti Norsupardi")
    st.write("**Email:** norizzaty.norsupard@gmail.com")
    st.write("**Phone:** (60) 19-223 8570")
    st.write("**LinkedIn:** [linkedin.com/in/norizzaty-norsupardi](https://linkedin.com/in/norizzaty-norsupardi)")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Education")

st.markdown("""    
**Bachelor of Information Technology (Hons) (AI track)**       
*Universiti Malaysia Kelantan*   
*2022 - Current*   

---

**Diploma in Multimedia Creative Animation**       
*Kolej Vokasional Kuala Krai*   
*2016 - 2019*   
            
---
            
**High School**     
*Sekolah Menengah Kebangsaan Jalan Kebun*   
*2014 - 2015*   
""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Work Experience")

st.markdown("""
**Tearista — Part Time**  
*Tealive*    
*Apr 2022 - Oct 2022*
- Provided excellent customer service and food handling. 

---             

**Video Editor — Contract**  
*Talentiv International Sdn Bhd*    
*Jul 2020 - Jun 2021*
- Edited dramas and TV programmes, and supported production with equipment handling and proposal drafting.  
            
--- 
            
**Video Editor — Internship**  
*Talentiv International Sdn Bhd*    
*Jan 2020 - Mar 2020*
- Support on-site production and deliver post-production editing for dramas and television programmes.           


""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Achievements")
st.markdown("""
- Involved in editing drama for TV3 and RTM (2020-2021).
- Involved in editing TV programme for RTM and JAKIM during internship (2020).
- Won 1st place in Traiblazer Cup Competition @ FSDK (2025).
- Won Best Business Model in Trailblazer Competition @ FSDK (2025).
- Achieved Dean's List for 3 semesters.
""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Skills")
st.markdown("""
- Video Editing
- Customer Service
- Digital Illustration
- UI/UX Design
""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Projects")
st.markdown("""
### Year 1
##### 1. Pet Grooming Service 
- Developing a booking system for pet grooming services using Python.  

---

### Year 2
##### 1. Student Supervision Management System
- Creating an application for student management (tracking class, attendance, and performance) and database for it.  

##### 2. Library Management System     
- Developing a library management system with authentication, borrowing, and returning features and inventory updates using Java.  

##### 3. Bus Schedule App      
- Designing a bus schedule app with real-time updates and reminder using Flutter and Dart.  

##### 4. Smart Crosswalk   
- Creating an IoT project for smart crosswalk system with sensors to detect pedestrian and traffic light control.  

---

### Year 3
##### 1. VendiMed  
- Developing a vending machine prototype that dispenses medications while integrated with an app for booking and scheduled pickup.  

##### 2. The Healthcare Disease Prediction for Diabetes  
- Creating a healthcare disease prediction system focusing on diabetes using Fuzzy Logic with several combinations of SVM, RF, and LSTM.  

##### 3. Regression For Flood Forecasting: Case Study in Gong Kedak, Terengganu  
- Building a flood forecasting system focusing on Gong Kedak, Terengganu using regression analysis.  

##### 4. Analysis Movie Rating  
- Analyzing movie ratings using Hadoop and MapReduce to find patterns and trends.  

##### 5. FBMKLCI Stock Price Prediction using LSTM  
- Predicting stock prices using LSTM neural networks and finding the best tuning parameters.  

##### 6. Predicting the Risk of Heart Disease using Multiple Machine Learning Algorithms  
- Developing a heart disease risk prediction model using several ML algorithms and comparing accuracy results.  
""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("Activities")
st.markdown("""
- Participated in PEWARIS KPT Siri 1 (2023).
- Joined the university's PRS (Pembimbing Rakan Siswa) club (2023/2024).
- Joined for PRS Exco Publicity (2023/2024).
""")

st.markdown("""
<hr style="border:1.8px solid #0b83b3; margin: 15px 0;">
""", unsafe_allow_html=True)

st.header("References")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Name:** Prof. Madya Ts. Dr. Hasyiya Karimah Binti Adli")
with col2:
    st.markdown("**Email:** hasyiya@umk.edu.my")
with col3:
    st.markdown("**Phone:** (60) 18-337 9687")
