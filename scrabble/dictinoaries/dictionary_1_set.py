# Simplest model of them all, in memory set


class Dictionary(object):
    @classmethod
    def make(cls, word_stream):
        """
        :param word_stream: clean stream of words to store. case sensitive !
        :return: an instance of this dictionary with the words stored
        """
        words = set()
        for word in word_stream:
            words.add(word)
        return cls(frozenset(words))

    def __init__(self, words):
        self._words = words

    def __contains__(self, item):
        return item in self._words


# TODO move this to a test class
def test():
    words = ['CAT', 'I', 'TOMORROW']

    model = Dictionary.make(words)

    assert 'CAT' in model
    assert 'I' in model
    assert 'TOMORROW' in model
    assert 'C' not in model

if __name__ == '__main__':
    test()



