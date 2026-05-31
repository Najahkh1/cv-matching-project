import pandas as pd

from models.tfidf_matcher import TFIDFMatcher
from models.semantic_matcher import SemanticMatcher


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


jobs_df = pd.read_csv("data/processed/jobs_processed.csv")
resumes_df = pd.read_csv("data/processed/resumes_processed.csv")

jobs_sample = jobs_df.head(500)

resume_index = 1
resume_text = resumes_df.iloc[resume_index]["resume_text"]

print(f"\nTesting resume index: {resume_index}")
print("\nResume text preview:")
print(resume_text[:500])


print("\nTF-IDF Resultaten")

tfidf_matcher = TFIDFMatcher()
tfidf_matcher.fit_transform_jobs(jobs_sample["job_text"])

tfidf_results = tfidf_matcher.match_resume_to_jobs(
    resume_text,
    jobs_sample,
    top_n=5
)

print(tfidf_results)


print("\nSemantic resultaten")

semantic_matcher = SemanticMatcher()
semantic_matcher.fit_jobs(jobs_sample["job_text"].tolist())

semantic_results = semantic_matcher.match_resume_to_jobs(
    resume_text,
    jobs_sample,
    top_n=5
)

print(semantic_results)