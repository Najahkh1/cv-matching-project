def __init__(self):

    self.stop_words = set(stopwords.words("english"))

    self.lemmatizer = WordNetLemmatizer()