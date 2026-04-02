import streamlit as st
from utils.resume_parser import *
from chatbot import get_jobs

# Page setup
st.set_page_config(page_title="AI Job Assistant", layout="centered")
st.title("💼 AI Job Search & Resume Analyzer")

# User inputs
role = st.text_input("Enter Job Role", "Python Developer")
location = st.text_input("Enter Location", "Bangalore")
file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("🔍 Search Jobs"):

    if file is None:
        st.warning("⚠️ Please upload resume first")
    else:
        # Resume analysis
        text = extract_text_from_pdf(file)
        skills = extract_skills(text)
        emails = extract_email(text)
        phones = extract_phone(text)
        score = resume_score(text)
        summary = summarize_resume(text)

        st.subheader("📄 Resume Content")
        st.text_area("Extracted Text", text[:500], height=200)
        st.subheader("🧠 Summary"); st.write(summary)
        st.subheader("💡 Skills Found"); st.write(skills)
        st.subheader("📧 Contact Info"); st.write("Email:", emails, "Phone:", phones)
        st.subheader("📊 Resume Score"); st.progress(score/100); st.write(f"Score: {score}/100")

        # Job Matching
        jobs = get_jobs(role, location)
        matched_jobs = []
        for job in jobs:
            for skill in skills:
                if skill.lower() in [s.lower() for s in job["skills"]]:
                    matched_jobs.append(job)
                    break

        st.subheader("🎯 Recommended Jobs Based on Your Resume")
        if matched_jobs:
            for job_data in matched_jobs:
                st.markdown(f"### ✅ {job_data['title']}\n💰 Salary: {job_data['salary']}\n📝 {job_data['desc']}")
        else:
            st.write("❌ No matching jobs found")

        # Skill gap
        st.subheader("📉 Skill Gap Analysis")
        all_required_skills = set(s.lower() for j in jobs for s in j["skills"])
        missing_skills = [s for s in all_required_skills if s not in [sk.lower() for sk in skills]]
        if missing_skills: st.write("❌ Missing Skills:", missing_skills)
        else: st.write("✅ You have all required skills!")