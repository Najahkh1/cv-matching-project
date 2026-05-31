from preprocessing.data_loader import DataLoader
from preprocessing.text_preprocessor import TextPreprocessor
from preprocessing.deduplicator import Deduplicator


def main():
    loader = DataLoader(
        "data/raw/job_descriptions.csv",
        "data/raw/resume_data.csv"
    )

    jobs_df, resumes_df = loader.load_all()

    preprocessor = TextPreprocessor()
    deduplicator = Deduplicator()

    jobs_df = preprocessor.clean_column_names(jobs_df)
    resumes_df = preprocessor.clean_column_names(resumes_df)

    jobs_df = preprocessor.combine_columns(
        jobs_df,
        [
            "Job Title",
            "Role",
            "Job Description",
            "skills",
            "Responsibilities",
            "Qualifications"
        ],
        "job_text"
    )

    resumes_df = preprocessor.combine_columns(
        resumes_df,
        [
            "skills",
            "responsibilities",
            "degree_names",
            "positions",
            "certification_skills",
            "job_position_name"
        ],
        "resume_text"
    )

    jobs_df = deduplicator.remove_duplicates(
        jobs_df,
        subset_columns=["job_text"]
    )

    jobs_df.to_csv("data/processed/jobs_processed.csv", index=False)
    resumes_df.to_csv("data/processed/resumes_processed.csv", index=False)

    print("Preprocessing completed.")
    print("Saved: data/processed/jobs_processed.csv")
    print("Saved: data/processed/resumes_processed.csv")
    print("Jobs shape:", jobs_df.shape)
    print("Resumes shape:", resumes_df.shape)


if __name__ == "__main__":
    main()