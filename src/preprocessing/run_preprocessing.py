from preprocessing.data_loader import DataLoader
from preprocessing.text_preprocessor import TextPreprocessor
from preprocessing.deduplicator import Deduplicator


JOBS_PATH = "data/raw/job_descriptions.csv"
RESUMES_PATH = "data/raw/resume_data.csv"

PROCESSED_JOBS_PATH = "data/processed/jobs_processed.csv"
PROCESSED_RESUMES_PATH = "data/processed/resumes_processed.csv"


def main():
    """
    Hoofdscript voor de preprocessing pipeline.

    Stappen:
    1. Laad vacature- en cv-data.
    2. Schoon kolomnamen op.
    3. Combineer relevante tekstkolommen.
    4. Verwijder dubbele vacatures.
    5. Sla de verwerkte datasets op.
    """
    loader = DataLoader(JOBS_PATH, RESUMES_PATH)

    try:
        jobs_df, resumes_df = loader.load_all()
    except FileNotFoundError as error:
        print(f"Fout bij laden van data: {error}")
        return

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
            "Qualifications",
        ],
        "job_text",
    )

    resumes_df = preprocessor.combine_columns(
        resumes_df,
        [
            "skills",
            "responsibilities",
            "degree_names",
            "positions",
            "certification_skills",
            "job_position_name",
        ],
        "resume_text",
    )

    jobs_df = deduplicator.remove_duplicates(
        jobs_df,
        subset_columns=["job_text"],
    )

    jobs_df.to_csv(PROCESSED_JOBS_PATH, index=False)
    resumes_df.to_csv(PROCESSED_RESUMES_PATH, index=False)

    print("\nPreprocessing succesvol afgerond")
    print("-" * 40)
    print(f"Opgeslagen: {PROCESSED_JOBS_PATH}")
    print(f"Opgeslagen: {PROCESSED_RESUMES_PATH}")
    print(f"Jobs shape: {jobs_df.shape}")
    print(f"Resumes shape: {resumes_df.shape}")


if __name__ == "__main__":
    main()