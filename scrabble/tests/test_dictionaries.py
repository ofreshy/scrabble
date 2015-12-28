
from testscenarios import TestWithScenarios

from scrabble.dictinoaries import dictionary_1_set, dictionary_2_sqllite


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

        self.assertEquals(len(dictionary), 3, "dictionary length")
        for word in words:
            self.assertTrue(word in dictionary, "missing word %s " % word)

    def test_words_are_not_duplicated(self):
        words = ['CAT', 'CATS', 'TOMORROW']
        duplicates = words

        dictionary = self.factory_func(words + duplicates)

        self.assertEquals(len(dictionary), len(words), "dictionary length")
        for word in words:
            self.assertTrue(word in dictionary, "missing word %s " % word)

    def test_that_non_alpha_numeric_words_are_removed(self):
        words = ['CAT', 'CATS', 'TOMORROW']
        non_alpha_numeric_words = ['TY^', '8te', '9ight']

        dictionary = self.factory_func(words + non_alpha_numeric_words)

        self.assertEquals(len(dictionary), len(words), "dictionary length")
        for word in words:
            self.assertTrue(word in dictionary, "missing word %s " % word)
        for word in non_alpha_numeric_words:
            self.assertFalse(word in dictionary, "extra word %s " % word)

    def test_that_white_spaces_are_removed(self):
        words = ['NEWLINE\n', 'SPACERIGHT ', ' SPACEBOTH ', '  TAB']
        expected_words = ['NEWLINE', 'SPACERIGHT', 'SPACEBOTH', 'TAB']

        dictionary = self.factory_func(words)

        self.assertEquals(len(dictionary), len(words), "dictionary length")
        for word in expected_words:
            self.assertTrue(word in dictionary, "missing word %s " % word)




