import pandas as pd

from models.semantic_matcher import SemanticMatcher


JOBS_SAMPLE_SIZE = 500
TEST_RESUME_INDEX = 6
TOP_N = 5


def main():
    jobs_df = pd.read_csv(
        "data/processed/jobs_processed.csv"
    )

    resumes_df = pd.read_csv(
        "data/processed/resumes_processed.csv"
    )

    jobs_sample = jobs_df.head(JOBS_SAMPLE_SIZE)

    matcher = SemanticMatcher()

    matcher.fit_jobs(
        jobs_sample["job_text"].tolist()
    )

    resume_text = resumes_df.iloc[
        TEST_RESUME_INDEX
    ]["resume_text"]

    matches = matcher.match_resume_to_jobs(
        resume_text,
        jobs_sample,
        top_n=TOP_N
    )

    print("\nSemantic Matching Resultaten\n")
    print(matches.to_string(index=False))


if __name__ == "__main__":
    main()