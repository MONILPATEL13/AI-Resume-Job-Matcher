"""Creates a fake resume and job description.  Needs: pip install reportlab"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

RESUME = """Asha Sample (fake resume for testing)
Summary
Student interested in building AI applications with Python.
Education
B.E. Information Technology, Demo College
Projects
Chatbot using Python, LLM APIs and Streamlit.
Sales report tool using pandas and Excel.
Skills
Python, pandas, Streamlit, Git, HTML, CSS, NLP"""

JOB = """Junior AI Engineer (sample job description)
We need a fresher who knows Python and builds LLM applications.
Required: Python, NLP, RAG, FAISS, Git, Streamlit, Docker.
You will create chatbot and document search features.
"""

page = canvas.Canvas("sample_data/resume.pdf", pagesize=A4)
for number, line in enumerate(RESUME.splitlines()):
    page.drawString(50, 790 - number * 20, line)
page.save()
Path("sample_data/job.txt").write_text(JOB, encoding="utf-8")
print("Sample files created")
