from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

class StemTokenizer(object):
    """
    StemTokenizer tokenizes words, removes stopwords and stems words
    in each document.
    """
    def __init__(self, stop_words):
        self.stop_words = stop_words
        self.stemmer    = SnowballStemmer(language='english')

    def __call__(self, articles):
        return [self.stemmer.stem(token)
                for token in word_tokenize(articles) if token not in self.stop_words]

    
    
class LemmaTokenizer(object):
    """
    LemmaTokenizer tokenizes words, removes stopwords and lemmatizes words
    in each document.
    """
    def __init__(self, stop_words):
        self.stop_words = stop_words
        self.lemmatizer = WordNetLemmatizer()
        
    def __call__(self, articles):
        return [self.lemmatizer.lemmatize(token) 
                for token in word_tokenize(articles) if token not in self.stop_words]