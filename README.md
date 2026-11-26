# AI Resume-Job Matcher

Compares a resume with a job description and shows a match score and missing skills.

## Features
- Reads PDF resumes and finds the main sections
- Finds matched and missing skills from a skill list
- Compares text with TF-IDF (optional: sentence embeddings)
- Command line and Streamlit screen

## How it works
```
Resume PDF --+
             +--> Text --> Skill matching (70%) ----+--> Score + missing skills
Job text ----+         --> Text similarity (30%) ---+
```
If no known skill is found in the job text, only text similarity is used.

## Tech stack
Python, scikit-learn, pdfplumber, Streamlit, sentence-transformers (optional)

## Setup
```bash
python -m pip install -r requirements.txt
python -m pip install sentence-transformers   # optional, for embeddings
```

## Run
```bash
python main.py sample_data/resume.pdf sample_data/job.txt
python -m streamlit run app.py
python -m unittest discover tests
```

## Limitations
- Only skills listed in `src/keywords.py` are detected
- It does not understand negation or skill level
- The 70/30 weights are a simple choice and have not been validated
- The score is a guide, not a prediction of hiring
- Scanned (image) PDFs are not supported

The files in `sample_data/` are fake.
