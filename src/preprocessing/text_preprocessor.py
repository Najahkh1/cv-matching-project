import re

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class TextPreprocessor:
    """
    Klasse voor het schoonmaken en voorbereiden van tekstdata voor NLP.
    """

    def __init__(self) -> None:
        """
        Initialiseert Engelse stopwoorden en de WordNet lemmatizer.
        """
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Verwijdert verborgen tekens en extra spaties uit kolomnamen.

        Parameters:
            df (pd.DataFrame): Dataset met originele kolomnamen.

        Returns:
            pd.DataFrame: Dataset met opgeschoonde kolomnamen.
        """
        df = df.copy()

        df.columns = (
            df.columns
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
        )

        return df

    def clean_text(self, text: str) -> str:
        """
        Maakt tekst schoon voor NLP-verwerking.

        Stappen:
        - zet tekst om naar lowercase
        - verwijdert speciale tekens
        - verwijdert dubbele spaties
        - verwijdert stopwoorden
        - past lemmatization toe

        Parameters:
            text (str): Originele tekst.

        Returns:
            str: Opgeschoonde tekst.
        """
        if pd.isna(text):
            return ""

        text = str(text).lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

        words = text.split()

        cleaned_words = [
            self.lemmatizer.lemmatize(word)
            for word in words
            if word not in self.stop_words
        ]

        return " ".join(cleaned_words)

    def combine_columns(
        self,
        df: pd.DataFrame,
        columns: list[str],
        new_column_name: str,
    ) -> pd.DataFrame:
        """
        Combineert meerdere tekstkolommen naar één nieuwe opgeschoonde tekstkolom.

        Ontbrekende kolommen worden automatisch aangemaakt als lege kolom,
        zodat de pipeline niet direct crasht bij kleine kolomverschillen.

        Parameters:
            df (pd.DataFrame): Dataset met tekstkolommen.
            columns (list[str]): Kolommen die gecombineerd worden.
            new_column_name (str): Naam van de nieuwe tekstkolom.

        Returns:
            pd.DataFrame: Dataset met nieuwe gecombineerde tekstkolom.
        """
        df = df.copy()

        for col in columns:
            if col not in df.columns:
                df[col] = ""

        df[new_column_name] = (
            df[columns]
            .fillna("")
            .astype(str)
            .agg(" ".join, axis=1)
        )

        df[new_column_name] = df[new_column_name].apply(self.clean_text)

        return df