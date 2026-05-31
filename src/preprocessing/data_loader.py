import pandas as pd


class DataLoader:
    """
    Class voor het laden van de vacature- en cv-datasets.
    """

    def __init__(self, jobs_path, resumes_path):
        self.jobs_path = jobs_path
        self.resumes_path = resumes_path

    def load_jobs(self):
        """
        Laadt de vacature dataset.
        """
        jobs_df = pd.read_csv(self.jobs_path)
        return jobs_df

    def load_resumes(self):
        """
        Laadt de cv dataset.
        """
        resumes_df = pd.read_csv(self.resumes_path)
        return resumes_df

    def load_all(self):
        """
        Laadt beide datasets tegelijk.
        """
        jobs_df = self.load_jobs()
        resumes_df = self.load_resumes()

        return jobs_df, resumes_df