from typing import Set, List
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


class StemTokenizer(object):
    """
    StemTokenizer tokenizes words, removes stopwords and stems words
    in each document.
    """
    def __init__(self, stop_words : Set[str]):
        """
        Sets the stop words and stemmer

        Params:
        -------
        stop_words : Set of stop words from NLTK. 
        """
        import re
        from nltk.stem import SnowballStemmer
        self.stop_words = stop_words
        self.stemmer    = SnowballStemmer(language='english')
        self.pattern    = re.compile('[\W_]+',re.UNICODE)
        
    def __call__(self, doc : str) -> List[str]:
        """

        """
        unfiltered_tokens = (self.pattern.sub("",self.stemmer.stem(token))  
                             for token in word_tokenize(doc.replace("\n", " ")) 
                             if token not in self.stop_words)

        return list(filter(lambda x : len(x) > 1, unfiltered_tokens))