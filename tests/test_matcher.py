import pandas as pd

from models.tfidf_matcher import TFIDFMatcher


jobs_df = pd.read_csv("data/processed/jobs_processed.csv")
resumes_df = pd.read_csv("data/processed/resumes_processed.csv")


matcher = TFIDFMatcher()


# Alleen eerste 10000 vacatures gebruiken
# anders duurt het te lang
jobs_sample = jobs_df.head(10000)

matcher.fit_transform_jobs(
    jobs_sample["job_text"]
)


# Eerste CV testen
resume_text = resumes_df.iloc[6]["resume_text"]


matches = matcher.match_resume_to_jobs(
    resume_text,
    jobs_sample,
    top_n=5
)


print(matches)

#ik heb 10.000 vacatures omdat 1.6 miljoen rows heel veel is. 