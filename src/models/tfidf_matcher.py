import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFMatcher:
    """
    TF-IDF matcher voor het vergelijken van cv-tekst met vacatureteksten.
    """

    def __init__(self) -> None:
        """
        Initialiseert de TF-IDF vectorizer.
        """
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.jobs_matrix = None

    def fit_transform_jobs(self, jobs_text: pd.Series) -> None:
        """
        Maakt een TF-IDF matrix van alle vacatureteksten.

        Parameters:
            jobs_text (pd.Series): Tekstkolom met opgeschoonde vacatureteksten.
        """
        self.jobs_matrix = self.vectorizer.fit_transform(jobs_text)

    def transform_resume(self, resume_text: str):
        """
        Zet één cv-tekst om naar dezelfde TF-IDF vectorruimte.

        Parameters:
            resume_text (str): Opgeschoonde cv-tekst.

        Returns:
            sparse matrix: TF-IDF vector van de cv-tekst.
        """
        return self.vectorizer.transform([resume_text])

    def match_resume_to_jobs(
        self,
        resume_text: str,
        jobs_df: pd.DataFrame,
        top_n: int = 5,
    ) -> pd.DataFrame:
        """
        Vergelijkt één cv met alle vacatures en geeft de top-N matches terug.

        Parameters:
            resume_text (str): Opgeschoonde cv-tekst.
            jobs_df (pd.DataFrame): Vacaturedataset.
            top_n (int): Aantal matches dat teruggegeven wordt.

        Returns:
            pd.DataFrame: Top-N vacatures met similarity score.
        """
        if self.jobs_matrix is None:
            raise ValueError("Voer eerst fit_transform_jobs() uit.")

        resume_vector = self.transform_resume(resume_text)

        similarity_scores = cosine_similarity(
            resume_vector,
            self.jobs_matrix,
        ).flatten()

        results_df = jobs_df.copy()
        results_df["similarity_score"] = similarity_scores

        top_matches = results_df.sort_values(
            by="similarity_score",
            ascending=False,
        ).head(top_n)

        output_columns = [
            "Job Title",
            "Role",
            "Company",
            "similarity_score",
            "Job Description",
        ]

        return top_matches[output_columns]