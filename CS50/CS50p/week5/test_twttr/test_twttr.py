from twttr import shorten

def test_no_vowel():
    assert shorten("CS50") == "CS50"


def test_with_vowel():
    assert shorten("Apple") == "ppl"
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
