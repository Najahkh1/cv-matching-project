import pandas as pd

from models.tfidf_matcher import TFIDFMatcher


def main():
    jobs_df = pd.read_csv(
        "data/processed/jobs_processed.csv"
    )

    resumes_df = pd.read_csv(
        "data/processed/resumes_processed.csv"
    )

    matcher = TFIDFMatcher()

    # Sample voor snellere tests
    jobs_sample = jobs_df.head(10000)

    matcher.fit_transform_jobs(
        jobs_sample["job_text"]
    )

    # Test CV
    resume_text = resumes_df.iloc[6]["resume_text"]

    matches = matcher.match_resume_to_jobs(
        resume_text,
        jobs_sample,
        top_n=5
    )

    print("\nTF-IDF Resultaten\n")
    print(matches)


if __name__ == "__main__":
    main()