from preprocessing.data_loader import DataLoader
from preprocessing.text_preprocessor import TextPreprocessor


loader = DataLoader(
    "data/raw/job_descriptions.csv",
    "data/raw/resume_data.csv"
)

preprocessor = TextPreprocessor()

jobs_df, resumes_df = loader.load_all()

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

print("Jobs kolommen:")
print(jobs_df.columns.tolist())

print("\nVoorbeeld job_text:")
print(jobs_df["job_text"].head())

print("\nResumes kolommen:")
print(resumes_df.columns.tolist())

print("\nVoorbeeld resume_text:")
print(resumes_df["resume_text"].head())