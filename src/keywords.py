"""Find known skills in a piece of text. Add more skills to this list."""
import re

SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript"],
    "HTML": ["html", "html5"],
    "CSS": ["css", "css3"],
    "Node.js": ["node.js", "nodejs"],
    "Express.js": ["express.js", "expressjs"],
    "React": ["react", "react.js", "reactjs"],
    "REST APIs": ["rest api", "rest apis", "restful"],
    "SQL": ["sql", "mysql", "postgresql"],
    "MongoDB": ["mongodb"],
    "Git": ["git", "github"],
    "Docker": ["docker"],
    "AWS": ["aws", "amazon web services"],
    "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"],
    "NLP": ["nlp", "natural language processing"],
    "LLMs": ["llm", "llms", "large language model", "large language models"],
    "RAG": ["rag", "retrieval-augmented generation", "retrieval augmented generation"],
    "FAISS": ["faiss"],
    "Prompt Engineering": ["prompt engineering"],
    "LangChain": ["langchain"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Streamlit": ["streamlit"],
    "FastAPI": ["fastapi"],
    "Flask": ["flask"],
    "Excel": ["excel"],
}


def find_skills(text):
    text = " ".join(text.lower().split())
    found = set()
    for skill, names in SKILLS.items():
        for name in names:
            # whole words only, so "java" does not match "javascript"
            if re.search(rf"(?<![a-z0-9]){re.escape(name)}(?![a-z0-9])", text):
                found.add(skill)
                break
    return found
