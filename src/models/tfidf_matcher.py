import pandas as pd
pd.set_option("display.max_columns", None)

pd.set_option("display.width", 200)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFMatcher:

    def __init__(self):
        """
        TF-IDF vectorizer object.
        """
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def fit_transform_jobs(self, jobs_text):
        """
        Maak TF-IDF matrix van vacatures.
        """
        self.jobs_matrix = self.vectorizer.fit_transform(jobs_text)

    def transform_resume(self, resume_text):
        """
        Zet resume tekst om naar TF-IDF vector.
        """
        return self.vectorizer.transform([resume_text])

    def match_resume_to_jobs(self, resume_text, jobs_df, top_n=5):
        """
        Zoek beste matches tussen een CV en vacatures.
        """

        resume_vector = self.transform_resume(resume_text)

        similarity_scores = cosine_similarity(
            resume_vector,
            self.jobs_matrix
        )

        similarity_scores = similarity_scores.flatten()

        jobs_df = jobs_df.copy()

        jobs_df["similarity_score"] = similarity_scores

        top_matches = jobs_df.sort_values(
            by="similarity_score",
            ascending=False
        ).head(top_n)

        return top_matches[
            [
                "Job Title",
                "Role",
                "Company",
                "similarity_score",
                "Job Description"
            ]
        ]
#TFidfvectorizaer zet tekst om naar cijfers/vectoren
#fit_transform_jobs() leert welke woorden bestaan? welke worden belangrijk zijn op basis van vacatures
#transform_resume() gebruikt dezelfde woordruimte voor cv's dit is belangrijk anders kan ik vertoren niet vergelijken
#cosine_similarity berken ik hiermee hoeveel lijken cv en vacature op elkaar => dan moet ik gaan testen