import pandas as pd

from models.semantic_matcher import SemanticMatcher


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


jobs_df = pd.read_csv("data/processed/jobs_processed.csv")
resumes_df = pd.read_csv("data/processed/resumes_processed.csv")


# Kleine sample gebruiken, anders duurt semantic embeddings te lang
jobs_sample = jobs_df.head(500)

matcher = SemanticMatcher()

matcher.fit_jobs(
    jobs_sample["job_text"].tolist()
)

resume_text = resumes_df.iloc[6]["resume_text"]

matches = matcher.match_resume_to_jobs(
    resume_text,
    jobs_sample,
    top_n=5
)

print(matches)