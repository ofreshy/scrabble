# Simplest model of them all, in memory set

from scrabble.dictinoaries.dictionary_builder import clean_word_stream


class Dictionary(object):
    @classmethod
    def make(cls, word_stream):
        """
        :param word_stream: clean stream of words to store. case sensitive !
        :return: an instance of this dictionary with the words stored
        """
        words = set()
        for word in clean_word_stream(word_stream):
            words.add(word)
        return cls(frozenset(words))

    def __init__(self, words):
        self._words = words
        # not sure if set is smart enough to remember
        # so save once as this is a frozen set
        self._length = len(words)

    def __len__(self):
        return self._length

    def __contains__(self, item):
        return item in self._words
