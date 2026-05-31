import re
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class TextPreprocessor:
    """
    Class voor het schoonmaken en voorbereiden van tekstdata.
    """

    def __init__(self):
        """
        Initialiseert stopwoorden en lemmatizer.
        """
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_column_names(self, df):
        """
        Verwijdert verborgen tekens en extra spaties uit kolomnamen.
        """
        df = df.copy()

        df.columns = (
            df.columns
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
        )

        return df

    def clean_text(self, text):
        """
        Maakt tekst schoon voor NLP:
        - zet tekst naar lowercase
        - verwijdert speciale tekens
        - verwijdert dubbele spaties
        - verwijdert stopwoorden
        - past lemmatization toe
        """
        if pd.isna(text):
            return ""

        text = str(text)
        text = text.lower()

        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()

        words = text.split()

        cleaned_words = []

        for word in words:
            if word not in self.stop_words:
                lemma = self.lemmatizer.lemmatize(word)
                cleaned_words.append(lemma)

        return " ".join(cleaned_words)

    def combine_columns(self, df, columns, new_column_name):
        """
        Combineert meerdere tekstkolommen naar één nieuwe tekstkolom.
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


# Uitleg:
#
# Deze class doet drie belangrijke dingen:
#
# 1. clean_column_names()
#    Maakt kolomnamen schoon, bijvoorbeeld '\ufeffjob_position_name'
#    wordt 'job_position_name'.
#
# 2. clean_text()
#    Maakt tekst geschikt voor NLP door lowercase, regex cleaning,
#    stopwords removal en lemmatization toe te passen.
#
# 3. combine_columns()
#    Combineert meerdere relevante kolommen naar één tekstkolom,
#    zoals job_text of resume_text.
#
# Dit is nodig voordat we TF-IDF, cosine similarity of embeddings gebruiken.