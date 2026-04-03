import streamlit as st
from utils.resume_parser import (
    extract_text_from_pdf,
    extract_skills,
    extract_email,
    extract_phone,
    resume_score,
    summarize_resume
)

# 🎯 Dummy job data (with skills)
def get_jobs(role, location):
    return [
        {"title": f"{role} at Infosys - {location}", "skills": ["python", "sql"]},
        {"title": f"{role} at TCS - {location}", "skills": ["java", "html"]},
        {"title": f"{role} at Wipro - {location}", "skills": ["python", "machine learning"]},
        {"title": f"{role} at Accenture - {location}", "skills": ["javascript", "css"]}
    ]

# 🎨 Page setup
st.set_page_config(page_title="Job Assistant", layout="centered")

st.title("💼 Job Search AI Assistant")

# 🔍 JOB INPUT
st.subheader("🔍 Enter Job Details")

role = st.text_input("Enter Job Role", "Python Developer")
location = st.text_input("Enter Location", "Bangalore")

# 📄 RESUME ANALYZER
st.subheader("📄 Upload Resume")

file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if file is not None:
    text = extract_text_from_pdf(file)

    # 🔹 Resume Analysis
    skills = extract_skills(text)
    emails = extract_email(text)
    phones = extract_phone(text)
    score = resume_score(text)
    summary = summarize_resume(text)

    # 📄 Show Resume Info
    st.subheader("📄 Resume Content")
    st.text_area("Extracted Text", text[:500], height=200)

    st.subheader("🧠 Summary")
    st.write(summary)

    st.subheader("💡 Skills Found")
    st.write(skills)

    st.subheader("📧 Contact Info")
    st.write("Email:", emails)
    st.write("Phone:", phones)

    st.subheader("📊 Resume Score")
    st.progress(score / 100)
    st.write(f"Score: {score}/100")

    # 🔥 JOB MATCHING (MAIN FEATURE)
    st.subheader("🎯 Recommended Jobs Based on Your Resume")

    jobs = get_jobs(role, location)
    matched_jobs = []

    for job in jobs:
        for skill in skills:
            if skill.lower() in [s.lower() for s in job["skills"]]:
                matched_jobs.append(job["title"])
                break

    if matched_jobs:
        for job in matched_jobs:	Q
            st.write("✅", job)
    else:
        st.write("❌ No matching jobs found")

st.write("✅ AI JOB MATCHING SYSTEM RUNNING")