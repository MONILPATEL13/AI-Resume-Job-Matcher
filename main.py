"""Usage: python main.py sample_data/resume.pdf sample_data/job.txt"""
import argparse
import json

from src.matcher import match
from src.parser import read_file


def main():
    parser = argparse.ArgumentParser(description="Match a resume with a job")
    parser.add_argument("resume", help="resume file (.pdf or .txt)")
    parser.add_argument("job", help="job description file (.txt or .pdf)")
    parser.add_argument("--method", choices=["tfidf", "embeddings"], default="tfidf")
    args = parser.parse_args()
    result = match(read_file(args.resume), read_file(args.job), args.method)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
