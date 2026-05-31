from preprocessing.data_loader import DataLoader


loader = DataLoader(
    "data/raw/job_descriptions.csv",
    "data/raw/resume_data.csv"
)

jobs_df, resumes_df = loader.load_all()

print("Jobs dataset:")
print(jobs_df.head())

print("\nAantal rijen en kolommen jobs:")
print(jobs_df.shape)

print("\nKolommen jobs:")
print(jobs_df.columns.tolist())

print("\nResumes dataset:")
print(resumes_df.head())

print("\nAantal rijen en kolommen resumes:")
print(resumes_df.shape)

print("\nKolommen resumes:")
print(resumes_df.columns.tolist())