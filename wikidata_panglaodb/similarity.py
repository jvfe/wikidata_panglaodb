"""Similarity checking functions"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def get_string_match(string1, string2):
    """Checks if the stemmed version of two strings is the same
    
    Sometimes matches from the reconciliation service return as false since 
    the item has few statements or no statements at all. To take care of those 
    cases we'll perform a simple string similarity check, using the stemmed version
    of both strings.

    Args:
        string1 (str): A string to compare.
        string2 (str): A string to compare.

    Returns:
        bool: If they match, return True, else return False.

    """
    tokenized = [[tokenized] for tokenized in [string1, string2]]

    ps = PorterStemmer()
    stemmed = [[ps.stem(w)] for tokens in tokenized for w in tokens]

    return stemmed[0] == stemmed[1]
