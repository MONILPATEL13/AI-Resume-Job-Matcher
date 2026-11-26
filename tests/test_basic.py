"""Usage: python -m unittest discover tests"""
import unittest

from src.keywords import find_skills
from src.matcher import match
from src.parser import read_file


class BasicTests(unittest.TestCase):
    def test_java_is_not_javascript(self):
        self.assertEqual(find_skills("I know JavaScript."), {"JavaScript"})

    def test_missing_skill_is_found(self):
        result = match("Skills\nPython", "Need Python and Docker")
        self.assertEqual(result["missing_skills"], ["Docker"])

    def test_same_text_scores_full(self):
        text = "Python developer with Docker"
        self.assertEqual(match(text, text)["score"], 100.0)

    def test_sample_files(self):
        result = match(read_file("sample_data/resume.pdf"),
                       read_file("sample_data/job.txt"))
        self.assertIn("RAG", result["missing_skills"])
        self.assertIn("skills", result["sections_found"])


if __name__ == "__main__":
    unittest.main()
