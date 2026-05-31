import pandas as pd

from models.tfidf_matcher import TFIDFMatcher
from models.semantic_matcher import SemanticMatcher


def main():

    print("Loading processed datasets...")

    jobs_df = pd.read_csv(
        "data/processed/jobs_processed.csv"
    )

    resumes_df = pd.read_csv(
        "data/processed/resumes_processed.csv"
    )

    # Kleine sample voor snelheid
    jobs_sample = jobs_df.head(500)

    # Alleen eerste 10 CV's evalueren
    resumes_sample = resumes_df.head(10)

    print("Initializing models...")

    tfidf_matcher = TFIDFMatcher()

    semantic_matcher = SemanticMatcher()

    print("Training TF-IDF model...")

    tfidf_matcher.fit_transform_jobs(
        jobs_sample["job_text"]
    )

    print("Creating semantic embeddings...")

    semantic_matcher.fit_jobs(
        jobs_sample["job_text"].tolist()
    )

    results = []

    print("Starting evaluation...")

    for index, row in resumes_sample.iterrows():

        resume_text = row["resume_text"]

        # TF-IDF
        tfidf_result = tfidf_matcher.match_resume_to_jobs(
            resume_text,
            jobs_sample,
            top_n=1
        )

        tfidf_top = tfidf_result.iloc[0]

        results.append({
            "resume_index": index,
            "model": "TF-IDF",
            "job_title": tfidf_top["Job Title"],
            "role": tfidf_top["Role"],
            "company": tfidf_top["Company"],
            "score": tfidf_top["similarity_score"]
        })

        # Semantic
        semantic_result = semantic_matcher.match_resume_to_jobs(
            resume_text,
            jobs_sample,
            top_n=1
        )

        semantic_top = semantic_result.iloc[0]

        results.append({
            "resume_index": index,
            "model": "Semantic",
            "job_title": semantic_top["Job Title"],
            "role": semantic_top["Role"],
            "company": semantic_top["Company"],
            "score": semantic_top["similarity_score"]
        })

    results_df = pd.DataFrame(results)

    print("\nEvaluation Results:\n")

    print(results_df)

    results_df.to_csv(
        "results/model_evaluation.csv",
        index=False
    )

    print("\nResults saved to:")
    print("results/model_evaluation.csv")


if __name__ == "__main__":
    main()