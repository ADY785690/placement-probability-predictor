import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Placement Intelligence Platform",
    layout="wide"
)

st.title("🎯 Placement Intelligence Platform")

st.markdown(
    "Predict placement probability, salary range, company tier and skill gaps."
)

st.sidebar.header("Student Profile")

cgpa = st.sidebar.slider("CGPA", 0.0, 10.0, 8.0)

dsa = st.sidebar.slider(
    "DSA Problems Solved",
    0,
    500,
    150
)

projects = st.sidebar.slider(
    "Projects Completed",
    0,
    20,
    5
)

internships = st.sidebar.slider(
    "Internships",
    0,
    5,
    1
)

communication = st.sidebar.slider(
    "Communication Skills",
    0,
    10,
    7
)

python_skill = st.sidebar.slider(
    "Python Skill",
    0,
    10,
    7
)

sql_skill = st.sidebar.slider(
    "SQL Skill",
    0,
    10,
    6
)

if st.sidebar.button("Generate Placement Report"):

    placement_score = min(
        (
            cgpa * 8
            + (dsa / 5)
            + projects * 4
            + internships * 8
            + communication * 2
        ),
        100
    )

    if placement_score >= 85:
        salary = "15-30 LPA"
        tier = "Tier 1"
    elif placement_score >= 70:
        salary = "8-15 LPA"
        tier = "Tier 2"
    else:
        salary = "4-8 LPA"
        tier = "Tier 3"

    resume_score = min(
        (
            projects * 8
            + internships * 15
            + cgpa * 4
        ),
        100
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Placement Probability",
        f"{placement_score:.0f}%"
    )

    col2.metric(
        "Expected Salary",
        salary
    )

    col3.metric(
        "Company Tier",
        tier
    )

    col4.metric(
        "Resume Score",
        f"{resume_score:.0f}/100"
    )

    st.divider()

    st.subheader("📊 Placement Readiness")

    chart_data = pd.DataFrame({
        "Metric": [
            "CGPA",
            "DSA",
            "Projects",
            "Communication",
            "Python",
            "SQL"
        ],
        "Score": [
            cgpa * 10,
            min(dsa / 5, 100),
            projects * 5,
            communication * 10,
            python_skill * 10,
            sql_skill * 10
        ]
    })

    fig = px.bar(
        chart_data,
        x="Metric",
        y="Score",
        title="Placement Readiness Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("🏢 Recommended Companies")

    companies = []

    if placement_score >= 85:
        companies = [
            "Amazon",
            "Microsoft",
            "JP Morgan",
            "Goldman Sachs",
            "Adobe"
        ]
    elif placement_score >= 70:
        companies = [
            "TCS Digital",
            "Accenture",
            "Infosys",
            "Deloitte"
        ]
    else:
        companies = [
            "Wipro",
            "Cognizant",
            "Capgemini"
        ]

    for company in companies:
        st.success(company)

    st.divider()

    st.subheader("📉 Skill Gap Analysis")

    gaps = []

    if python_skill < 7:
        gaps.append("Improve Python")

    if sql_skill < 7:
        gaps.append("Improve SQL")

    if dsa < 150:
        gaps.append("Solve More DSA Problems")

    if communication < 7:
        gaps.append("Improve Communication")

    if len(gaps) == 0:
        st.success("No Major Skill Gaps Found")
    else:
        for gap in gaps:
            st.warning(gap)

    st.divider()

    st.subheader("🛣 90-Day Placement Roadmap")

    roadmap = [
        "Month 1: DSA + SQL",
        "Month 2: Projects + Resume",
        "Month 3: Mock Interviews + Applications"
    ]

    for step in roadmap:
        st.write("✅", step)

    st.divider()

    st.subheader("📥 Download Placement Report")

    report = pd.DataFrame({
        "Metric": [
            "Placement Probability",
            "Expected Salary",
            "Company Tier",
            "Resume Score"
        ],
        "Value": [
            placement_score,
            salary,
            tier,
            resume_score
        ]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "placement_report.csv",
        "text/csv"
    )

else:
    st.info(
        "Fill profile details and click Generate Placement Report"
    )
