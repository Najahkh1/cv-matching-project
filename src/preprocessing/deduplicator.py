import pandas as pd


class Deduplicator:
    """
    Klasse voor het verwijderen van dubbele rijen uit datasets.
    """

    def remove_duplicates(
        self,
        df: pd.DataFrame,
        subset_columns: list
    ) -> pd.DataFrame:
        """
        Verwijdert dubbele rijen op basis van opgegeven kolommen.

        Parameters:
            df (pd.DataFrame): Dataset die gecontroleerd wordt.
            subset_columns (list): Kolommen waarop duplicaten worden bepaald.

        Returns:
            pd.DataFrame: Dataset zonder duplicaten.
        """

        if df.empty:
            print("Waarschuwing: dataset is leeg.")
            return df

        df = df.copy()

        before = len(df)

        df = df.drop_duplicates(subset=subset_columns)

        after = len(df)
        removed = before - after

        print("\nDeduplicatie overzicht")
        print("-" * 30)
        print(f"Aantal rijen voor deduplicatie : {before}")
        print(f"Aantal rijen na deduplicatie   : {after}")
        print(f"Aantal verwijderde duplicaten  : {removed}")

        return df