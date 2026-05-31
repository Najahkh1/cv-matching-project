class Deduplicator:
    """
    Class voor het verwijderen van dubbele rijen uit datasets.
    """

    def remove_duplicates(self, df, subset_columns):
        """
        Verwijdert dubbele rijen op basis van gekozen kolommen.
        """
        df = df.copy()

        before = len(df)

        df = df.drop_duplicates(subset=subset_columns)

        after = len(df)

        print(f"Aantal rijen voor deduplicatie: {before}")
        print(f"Aantal rijen na deduplicatie: {after}")
        print(f"Aantal verwijderde duplicaten: {before - after}")

        return df
#De vacaturedataset is heel groot: 1.615.940 rijen. Als veel vacatures inhoudelijk hetzelfde zijn,
#  krijgt de model steeds dezelfde matches terug. Deduplicatie maakt de resultaten eerlijker, sneller en beter uitlegbaar. 
