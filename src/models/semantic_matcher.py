import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticMatcher:

    def __init__(self):
        """
        Semantic embedding model laden.
        """
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def fit_jobs(self, jobs_text):
        """
        Maak embeddings voor vacatures.
        """
        self.job_embeddings = self.model.encode(
            jobs_text,
            show_progress_bar=True
        )

    def match_resume_to_jobs(self, resume_text, jobs_df, top_n=5):
        """
        Zoek semantic matches tussen CV en vacatures.
        """

        resume_embedding = self.model.encode([resume_text])

        similarity_scores = cosine_similarity(
            resume_embedding,
            self.job_embeddings
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
#deze code kijkt vooral woord overlap en semactic model kijkt naar betekenis/context
# dus synoniemen, functierelatie, context en semantiche overeenkomsten