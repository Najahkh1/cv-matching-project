import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticMatcher:
    """
    Semantic matcher op basis van Sentence Transformers.
    """

    def __init__(self) -> None:
        """
        Laadt het embedding model.
        """
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.job_embeddings = None

    def fit_jobs(self, jobs_text: pd.Series) -> None:
        """
        Genereert embeddings voor alle vacatures.
        """
        self.job_embeddings = self.model.encode(
            jobs_text,
            show_progress_bar=True
        )

    def match_resume_to_jobs(
        self,
        resume_text: str,
        jobs_df: pd.DataFrame,
        top_n: int = 5
    ) -> pd.DataFrame:
        """
        Vergelijkt een cv met alle vacatures
        en retourneert de top-N matches.
        """

        if self.job_embeddings is None:
            raise ValueError(
                "Voer eerst fit_jobs() uit."
            )

        resume_embedding = self.model.encode(
            [resume_text]
        )

        similarity_scores = cosine_similarity(
            resume_embedding,
            self.job_embeddings
        ).flatten()

        results_df = jobs_df.copy()
        results_df["similarity_score"] = similarity_scores

        top_matches = results_df.sort_values(
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