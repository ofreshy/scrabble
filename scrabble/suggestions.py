"""
Suggests words based on your letters
"""

from itertools import permutations


def suggest(letters, dictionary, max_length=7):
    """

    :param letters: string with all letters
    :param dictionary: of words
    :param max_length: of words suggested
    :return: dictionary with keys as word length, and values are lists of words
    """
    answer = {}
    for r in range(1, min(len(letters)+1, max_length)):
        perms = permutations(letters, r)
        found_words = list({"".join(w) for w in perms if "".join(w) in dictionary})
        found_words.sort()
        answer[r] = found_words
    return answer


if __name__ == "__main__":
    print (suggest("ABCAT", ["CAT", "CATA"]))


