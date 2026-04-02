def get_jobs(role, location):
    return [
        {"title": f"{role} at Infosys - {location}", "skills": ["python", "sql"], "salary":"₹6–10 LPA", "desc":"Backend & data projects"},
        {"title": f"{role} at TCS - {location}", "skills": ["java", "html"], "salary":"₹4–8 LPA", "desc":"Enterprise applications"},
        {"title": f"{role} at Wipro - {location}", "skills": ["python", "machine learning"], "salary":"₹5–12 LPA", "desc":"AI/ML apps"},
        {"title": f"{role} at Accenture - {location}", "skills": ["javascript", "css"], "salary":"₹5–9 LPA", "desc":"Frontend web apps"}
    ]