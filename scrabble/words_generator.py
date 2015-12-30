from itertools import permutations
import re


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



