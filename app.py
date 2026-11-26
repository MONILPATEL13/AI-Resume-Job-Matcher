"""Web screen.  Usage: streamlit run app.py"""
import streamlit as st

from src.matcher import match
from src.parser import extract_text

st.title("AI Resume-Job Matcher")
resume = st.file_uploader("Upload resume (PDF)", type="pdf")
job = st.text_area("Paste the job description", height=220)
method = st.radio("Text comparison method", ["tfidf", "embeddings"], horizontal=True)

if st.button("Match", disabled=not (resume and job.strip())):
    try:
        with st.spinner("Comparing"):
            result = match(extract_text(resume), job, method)
    except ImportError:
        st.error("Embeddings need: python -m pip install sentence-transformers")
        st.stop()
    except Exception as error:
        st.error(f"Could not match: {error}")
        st.stop()

    st.metric("Match score", f"{result['score']}%")
    st.progress(min(result["score"] / 100, 1.0))
    left, right = st.columns(2)
    left.subheader("Matched skills")
    left.write(", ".join(result["matched_skills"]) or "None found")
    right.subheader("Missing skills")
    right.write(", ".join(result["missing_skills"]) or "None found")
    st.subheader("Suggestions")
    for tip in result["tips"] or ["No suggestions."]:
        st.write("- " + tip)
