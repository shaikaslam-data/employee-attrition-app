# =========================================================
# IMPORT LIBRARIES
# =========================================================

import streamlit as st
import pandas as pd
import pickle
import statsmodels.api as sm

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# =========================================================
# LOGIN SYSTEM
# =========================================================

# Session state keeps user logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Sidebar login
st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Login button
if st.sidebar.button("Submit"):

    # Change these credentials if needed
    if username == "shaik" and password == "1111":
        st.session_state.logged_in = True
    else:
        st.sidebar.error("Invalid Username or Password")

# Stop app if not logged in
if not st.session_state.logged_in:
    st.stop()

# =========================================================
# TITLE
# =========================================================

st.title("Employee Attrition Prediction System")

st.markdown("Predict whether an employee is likely to leave the company")

st.markdown("---")

# =========================================================
# CATEGORY MAPPINGS
# =========================================================

job_level_map = {
    "Entry": 0,
    "Mid": 1,
    "Senior": 2
}

company_reputation_map = {
    "Poor": 0,
    "Fair": 1,
    "Good": 2,
    "Excellent": 3
}

job_satisfaction_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2,
    "Very High": 3
}

work_life_balance_map = {
    "Poor": 0,
    "Fair": 1,
    "Good": 2,
    "Excellent": 3
}

# =========================================================
# INPUT SECTION
# =========================================================

col1, col2 = st.columns(2)

# ---------------- LEFT COLUMN ----------------

with col1:

    # Dropdown input
    job_level_text = st.selectbox(
        "Job Level",
        ["Entry", "Mid", "Senior"]
    )

    work_life_balance_text = st.selectbox(
        "Work Life Balance",
        ["Poor", "Fair", "Good", "Excellent"]
    )

    company_reputation_text = st.selectbox(
        "Company Reputation",
        ["Poor", "Fair", "Good", "Excellent"]
    )

    job_satisfaction_text = st.selectbox(
        "Job Satisfaction",
        ["Low", "Medium", "High", "Very High"]
    )

    # Yes/No inputs
    remote_work_text = st.selectbox(
        "Remote Work",
        ["No", "Yes"]
    )

    overtime_text = st.selectbox(
        "Overtime",
        ["No", "Yes"]
    )

    gender_text = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

# ---------------- RIGHT COLUMN ----------------

with col2:

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married"]
    )

    company_size = st.selectbox(
        "Company Size",
        ["Large", "Small"]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=0
    )

    number_of_promotions = st.number_input(
        "Number of Promotions",
        min_value=0
    )

    number_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0
    )

# =========================================================
# ENCODING USER INPUTS
# =========================================================

# Convert category text into numbers

job_level = job_level_map[job_level_text]

work_life_balance = work_life_balance_map[work_life_balance_text]

company_reputation = company_reputation_map[company_reputation_text]

job_satisfaction = job_satisfaction_map[job_satisfaction_text]

# Convert Yes/No to 1/0

remote_work = 1 if remote_work_text == "Yes" else 0

overtime = 1 if overtime_text == "Yes" else 0

gender_Male = 1 if gender_text == "Male" else 0

marital_status_Single = 1 if marital_status == "Single" else 0

marital_status_Married = 1 if marital_status == "Married" else 0

company_size_Small = 1 if company_size == "Small" else 0

# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("Predict Attrition"):

    # Create dataframe
    input_data = pd.DataFrame({

        'job_level': [job_level],

        'marital_status_Single': [marital_status_Single],

        'marital_status_Married': [marital_status_Married],

        'remote_work': [remote_work],

        'work_life_balance': [work_life_balance],

        'company_reputation': [company_reputation],

        'gender_Male': [gender_Male],

        'distance_from_home': [distance_from_home],

        'number_of_promotions': [number_of_promotions],

        'number_of_dependents': [number_of_dependents],

        'company_size_Small': [company_size_Small],

        'overtime': [overtime],

        'job_satisfaction': [job_satisfaction]

    })

    # Add constant for statsmodels
    input_data = sm.add_constant(input_data)

    # =====================================================
    # PROBABILITY PREDICTION
    # =====================================================

    probability = model.predict(input_data)[0]

    # =====================================================
    # THRESHOLD CONVERSION
    # =====================================================

    threshold = 0.50

    prediction = 1 if probability >= threshold else 0

    st.markdown("---")

    st.subheader("Prediction Result")

    st.write(f"Attrition Probability: {probability:.2f}")

    # Final class output
    if prediction == 1:
        st.error("Employee Likely to Leave")
    else:
        st.success("Employee Likely to Stay")