import PyPDF2
import re

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def extract_skills(text):
    skills_list = ["python","java","c++","sql","machine learning","ai","html","css","javascript","data science"]
    return [skill for skill in skills_list if skill.lower() in text.lower()]

def extract_email(text):
    return re.findall(r'\S+@\S+', text)

def extract_phone(text):
    return re.findall(r'\d{10}', text)

def resume_score(text):
    score = 0
    text = text.lower()
    if "python" in text: score += 20
    if "project" in text: score += 20
    if "experience" in text: score += 20
    if "education" in text: score += 20
    if "skills" in text: score += 20
    return score

def summarize_resume(text):
    return text[:200]+"..."