import pandas as pd


class DataLoader:
    """
    Klasse voor het laden van vacature- en cv-datasets.
    """

    def __init__(self, jobs_path: str, resumes_path: str):
        self.jobs_path = jobs_path
        self.resumes_path = resumes_path

    def load_jobs(self) -> pd.DataFrame:
        """
        Laadt de vacaturedataset.

        Returns:
            pd.DataFrame: DataFrame met vacaturegegevens.
        """
        try:
            return pd.read_csv(self.jobs_path)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Vacaturebestand niet gevonden: {self.jobs_path}"
            )

    def load_resumes(self) -> pd.DataFrame:
        """
        Laadt de cv-dataset.

        Returns:
            pd.DataFrame: DataFrame met cv-gegevens.
        """
        try:
            return pd.read_csv(self.resumes_path)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"CV-bestand niet gevonden: {self.resumes_path}"
            )

    def load_all(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Laadt beide datasets.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame]:
            Vacaturedataset en cv-dataset.
        """
        jobs_df = self.load_jobs()
        resumes_df = self.load_resumes()

        return jobs_df, resumes_df