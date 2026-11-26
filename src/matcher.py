"""Score a resume against a job description."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .keywords import find_skills
from .parser import split_sections

SKILL_WEIGHT = 0.7
TEXT_WEIGHT = 0.3


def tfidf_similarity(resume, job):
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2),
                                 sublinear_tf=True)
    vectors = vectorizer.fit_transform([resume, job])
    return float(cosine_similarity(vectors[0], vectors[1])[0, 0])


def embedding_similarity(resume, job):
    """Optional: compares meaning. Needs: pip install sentence-transformers"""
    from sentence_transformers import SentenceTransformer, util

    model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(text):
        # The model reads short text only, so average over small chunks.
        words = text.split()
        chunks = [" ".join(words[i:i + 150]) for i in range(0, len(words), 150)]
        return model.encode(chunks, convert_to_tensor=True).mean(dim=0)

    return max(0.0, float(util.cos_sim(embed(resume), embed(job))))


def match(resume, job, method="tfidf"):
    if not resume.strip() or not job.strip():
        raise ValueError("Resume and job description must not be empty.")
    similarity = embedding_similarity if method == "embeddings" else tfidf_similarity
    text_score = min(similarity(resume, job), 1.0)

    wanted = find_skills(job)
    have = find_skills(resume)
    matched = sorted(wanted & have)
    missing = sorted(wanted - have)

    if wanted:
        skill_score = len(matched) / len(wanted)
        score = SKILL_WEIGHT * skill_score + TEXT_WEIGHT * text_score
    else:
        skill_score, score = None, text_score

    sections = split_sections(resume)
    tips = [f"No clear '{name}' section found."
            for name in ("education", "projects", "skills") if name not in sections]
    if missing:
        tips.append("The job asks for: " + ", ".join(missing)
                    + ". Add these only if you really have them; otherwise learn them.")
    if not wanted:
        tips.append("No known skills found in the job text; score uses text similarity only.")

    return {
        "score": round(score * 100, 1),
        "skill_score": None if skill_score is None else round(skill_score * 100, 1),
        "text_score": round(text_score * 100, 1),
        "matched_skills": matched,
        "missing_skills": missing,
        "sections_found": list(sections),
        "tips": tips,
    }
