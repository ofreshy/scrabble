
from testscenarios import TestWithScenarios

from scrabble.dictionaries import dictionary_1_set, dictionary_2_sqllite


def make_dictionary_sqllite():
    def make(word_stream):
        return dictionary_2_sqllite.Dictionary.make(word_stream=word_stream, db_name="test_words.sqlite")
    return make


class TestDictionaries(TestWithScenarios):
    scenarios = [
        ("dictionary_set", {"factory_func": dictionary_1_set.Dictionary.make}),
        ("dictionary_sql", {"factory_func": make_dictionary_sqllite()}),
    ]

    def test_empty_dict_has_length_of_0(self):
        words = []

        dictionary = self.factory_func(words)

        self.assertEquals(len(dictionary), 0, "dictionary length")

    def test_words_in_dictionary(self):
        words = ['CAT', 'CATS', 'TOMORROW']

        dictionary = self.factory_func(words)

        self.assertWordsIn(words, dictionary)

    def test_words_are_not_duplicated(self):
        words = ['CAT', 'CATS', 'TOMORROW']

        dictionary = self.factory_func(words * 2)

        self.assertWordsIn(words, dictionary)

    def test_that_non_alpha_numeric_words_are_removed(self):
        words = ['CAT', 'CATS', 'TOMORROW']
        non_alpha_numeric_words = ['TY^', '8te', '9ight']

        dictionary = self.factory_func(words + non_alpha_numeric_words)

        self.assertWordsIn(words, dictionary)
        self.assertWordsOut(non_alpha_numeric_words, dictionary)

    def test_that_white_spaces_are_removed(self):
        words = ['NEWLINE\n', 'SPACERIGHT ', ' SPACEBOTH ', '  TAB']
        expected_words = ['NEWLINE', 'SPACERIGHT', 'SPACEBOTH', 'TAB']

        dictionary = self.factory_func(words)

        self.assertWordsIn(expected_words, dictionary)

    def assertWordsIn(self, words, dictionary):
        expected = {word: True for word in words}
        actual = {word: word in dictionary for word in words}
        self.assertEquals(expected, actual)

    def assertWordsOut(self, words, dictionary):
        expected = {word: False for word in words}
        actual = {word: word in dictionary for word in words}
        self.assertEquals(expected, actual)

