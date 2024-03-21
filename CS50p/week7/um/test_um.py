from um import count

def test_default():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um,") == 1


def test_sentence():
    assert count("Um, thanks, um...") == 2


def test_word_sentence():
    assert count("Um, thanks for the album.") == 1
