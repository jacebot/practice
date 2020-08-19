import string

alphabet = list(string.ascii_lowercase)

def is_pangram(sentence: str):
    sentenceChars = set(sentence.lower())
    for c in alphabet:
        if c not in sentenceChars:
            return False
    return True
