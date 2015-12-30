from itertools import product, permutations
import re

from scrabble.constants import LETTERS

PATTERN = re.compile(r'(\w,)*(\w)+$')


def generate_sequences(pattern, free_letters):
    """
    Generate all possible sequences for the given pattern using some / all the free letters

    :param str pattern: in the format of '_,_,_' with fixed letters replacing underscores
    :param free_letters: to fill in
    :return: all possible sequences for pattern and letters
    """
    if not PATTERN.match(pattern):
        raise AssertionError('pattern %s is invalid. Use _,_,_ pattern' % pattern)

    num_of_slots = pattern.count('_')
    # we must have free letters as number of slots
    assert num_of_slots <= len(free_letters)

    fixed_letters = [l.upper() for l in pattern if l.isalpha()]
    # sort the letters so we can assure order of sequence
    free_letters = "".join(sorted(free_letters.upper()))

    if num_of_slots == 0:
        # This means that all letters are fixed
        perms = [fixed_letters]
    elif len(fixed_letters) == 0:
        # This means that there are no constraints
        perms = permutations(free_letters)
    else:
        # This means that we got constraints
        # Take advantage of the format string method {} and tuple flattening *
        pattern = pattern.replace('_', '{}').replace(',', '')
        # This () creates a generator from a generator
        perms = (pattern.format(*p) for p in permutations(free_letters, num_of_slots))

    # Ready to generate sequences!
    for perm in perms:
        yield "".join(perm)


def generate_patterns(fixed_letters, max_left=7, max_right=7, min_letters=1, max_letters=7):
    """

    :param str fixed_letters: such as M,_,E M,E etc.  _ means fixed but empty (middle slot)
    :param int max_left: allowed spaces left from the last fixed letter
    :param int max_right: allowed spaces right from the first fixed letter
    :param int min_letters:
    :param int max_letters:
    :return:
    """
    if fixed_letters == '_':
        # There are no letter constrains, so only constraints are spaces
        real_max_letters = min(max(max_left, max_right), max_letters) + 1
        real_min_letters = min(max(max_left, max_right), min_letters)
        real_range = range(real_min_letters, real_max_letters)
        patterns = (",".join(['_'] * r) for r in real_range)

    for p in patterns:
        yield p


def generate_hands(letters):
    num_of_jokers = letters.count('*')
    if num_of_jokers:
        combinations = product(LETTERS, repeat=num_of_jokers)
        pattern = letters.replace('*', '{}')
        hands = (pattern.format(*h) for h in combinations)
    else:
        hands = [letters]

    for hand in hands:
        yield hand


def generate_words(dictionary, hands_generator, pattern_generator):
    for hand in hands_generator:
        for pattern in pattern_generator:
            for sequence in generate_sequences(pattern, hand):
                if sequence in dictionary:
                    yield sequence

if 1 == 0:
    eligible_words = []
    dictionary = None
    free_letters = ''
    fixed_letters = '_'

    hands_generator = generate_hands(free_letters)
    pattern_generator = generate_patterns(fixed_letters)
    word_generator = generate_words(dictionary, hands_generator, pattern_generator)
    # TODO - Instead, implement a deque with a value for each word
    eligible_words = [w for w in word_generator]


