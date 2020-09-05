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

    tokenized1 = word_tokenize(string1)
    tokenized2 = word_tokenize(string2)

    ps = PorterStemmer()
    stemmed1 = [ps.stem(w) for w in tokenized1]
    stemmed2 = [ps.stem(w) for w in tokenized2]

    if stemmed1 == stemmed2:
        return True
    else:
        return False
