from unittest2 import TestCase

from scrabble import words_generator


class TestSequenceGenerator(TestCase):
    def test_with_no_constrains_one_letter(self):
        pattern = '_'
        free_letters = 'A'
        expected = ['A']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_with_no_constrains_three_letters(self):
        pattern = '_,_,_'
        free_letters = 'CAT'
        expected = ['ACT', 'ATC', 'CAT', 'CTA', 'TAC', 'TCA']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_all_fixed_pattern_returns_one_word(self):
        pattern = 'C,A,T'
        free_letters = ''
        expected = ['CAT']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_two_slots_with_one_fixed_letter(self):
        pattern = 'C,_'
        free_letters = 'A'
        expected = ['CA']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_three_slots_with_one_fixed_letters(self):
        pattern = 'C,_,_'
        free_letters = 'AT'
        expected = ['CAT', 'CTA']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_three_slots_with_two_fixed_letters(self):
        pattern = 'C,_,T'
        free_letters = 'A'
        expected = ['CAT']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_two_consectutive_fixed_letters(self):
        pattern = 'C,A,_'
        free_letters = 'T'
        expected = ['CAT']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_with_replacement(self):
        pattern = 'C,A,_'
        free_letters = 'TRB'
        expected = ['CAB', 'CAR', 'CAT']

        actual = list(words_generator.generate_sequences(pattern, free_letters))

        self.assertEquals(expected, actual)

    def test_invalid_pattern_not_enough_free_letters(self):
        with self.assertRaises(AssertionError):
            # Odd, but you got to force the generator
            # otherwise the python3 interpreter will not
            # evaluate any line in the function!
            list(words_generator.generate_sequences("_", ''))

    def test_invalid_pattern_not_allowed_chars(self):
        with self.assertRaises(AssertionError):
            # Odd, but you got to force the generator
            # otherwise the python3 interpreter will not
            # evaluate any line in the function!
            list(words_generator.generate_sequences(";_", 'AB'))

    def test_invalid_pattern_invalid_format(self):
        with self.assertRaises(AssertionError):
            # Odd, but you got to force the generator
            # otherwise the python3 interpreter will not
            # evaluate any line in the function!
            list(words_generator.generate_sequences("_,_,", 'AB'))



