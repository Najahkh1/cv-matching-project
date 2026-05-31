import pandas as pd

from models.tfidf_matcher import TFIDFMatcher
from models.semantic_matcher import SemanticMatcher


JOBS_SAMPLE_SIZE = 500
TEST_RESUME_INDEX = 1
TOP_N = 5


def main():
    jobs_df = pd.read_csv(
        "data/processed/jobs_processed.csv"
    )

    resumes_df = pd.read_csv(
        "data/processed/resumes_processed.csv"
    )

    jobs_sample = jobs_df.head(JOBS_SAMPLE_SIZE)

    resume_text = resumes_df.iloc[
        TEST_RESUME_INDEX
    ]["resume_text"]

    print(f"\nTesting resume index: {TEST_RESUME_INDEX}")

    print("\nResume text preview:")
    print(resume_text[:500])

    print("\nTF-IDF Resultaten")

    tfidf_matcher = TFIDFMatcher()
    tfidf_matcher.fit_transform_jobs(
        jobs_sample["job_text"]
    )

    tfidf_results = tfidf_matcher.match_resume_to_jobs(
        resume_text,
        jobs_sample,
        top_n=TOP_N
    )

    print(tfidf_results.to_string(index=False))

    print("\nSemantic Resultaten")

    semantic_matcher = SemanticMatcher()
    semantic_matcher.fit_jobs(
        jobs_sample["job_text"].tolist()
    )

    semantic_results = semantic_matcher.match_resume_to_jobs(
        resume_text,
        jobs_sample,
        top_n=TOP_N
    )

    print(semantic_results.to_string(index=False))

    print("\nBeste TF-IDF match:")
    print(
        tfidf_results.iloc[0][
            ["Job Title", "Role", "similarity_score"]
        ]
    )

    print("\nBeste Semantic match:")
    print(
        semantic_results.iloc[0][
            ["Job Title", "Role", "similarity_score"]
        ]
    )


if __name__ == "__main__":
    main()