import streamlit as st

st.title("🎯 Placement Probability Predictor")

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)

dsa = st.number_input("DSA Problems Solved", 0, 1000, 100)

internships = st.number_input("Internships", 0, 10, 1)

projects = st.number_input("Projects", 0, 20, 3)

communication = st.slider("Communication Score", 0, 10, 7)

if st.button("Predict"):

    score = (
        cgpa * 8 +
        min(dsa / 5, 20) +
        internships * 10 +
        projects * 4 +
        communication * 3
    )

    probability = min(score, 100)

    st.success(f"Placement Chance: {probability:.1f}%")

    if probability >= 80:
        st.success("Estimated Salary: ₹12-25 LPA")
    elif probability >= 60:
        st.info("Estimated Salary: ₹6-12 LPA")
    else:
        st.warning("Estimated Salary: ₹3-6 LPA")
