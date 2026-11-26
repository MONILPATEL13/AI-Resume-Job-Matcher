"""Read a resume and split it into sections."""
from pathlib import Path

import pdfplumber

HEADINGS = {
    "summary": ["summary", "professional summary", "profile", "objective"],
    "education": ["education"],
    "experience": ["experience", "work experience", "internships"],
    "projects": ["projects", "academic projects"],
    "skills": ["skills", "technical skills"],
    "certifications": ["certifications", "certificates"],
}


def extract_text(pdf_file):
    """pdf_file can be a file path or an uploaded file object."""
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages).strip()
    if not text:
        raise ValueError("No text found. This may be a scanned (image) PDF.")
    return text


def read_file(path):
    """Read a .pdf or .txt file."""
    path = Path(path)
    if path.suffix.lower() == ".pdf":
        return extract_text(path)
    return path.read_text(encoding="utf-8")


def split_sections(text):
    sections, current = {}, None
    for line in text.splitlines():
        title = line.strip().lower().rstrip(":")
        match = next((name for name, words in HEADINGS.items() if title in words), None)
        if match:
            current = match
            sections.setdefault(current, "")
        elif current:
            sections[current] += line + "\n"
    return sections
