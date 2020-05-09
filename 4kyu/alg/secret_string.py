"""""
task from codewars.com

There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string.
 In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""
import numpy as np


def set_true(map, elem):
    for e in map:
        if e[0] == elem:
            e[1] = True
            break


def reset_map(map) -> str:
    """"
    :param map -> list of pair, letters and bool flag

    :return next letter
    """
    letter = None

    for i in range(len(map)):
        if map[i][1] == False:
            letter = map[i]
        else:
            map[i][1] = False
    map.remove(letter)
    return letter[0]


def remove_letter_from_triplets(triplets, letter):
    for i in range(len(triplets)):
        triplets[i] = list(filter(lambda x: x != letter, triplets[i]))
    return list(filter(lambda x: len(x) > 0, triplets))


def recoverSecret(triplets):
    t = triplets
    letters = set(np.ravel(triplets))
    letters = list(map(lambda x: [x, False], letters))
    secret: str = ''
    size = len(letters)
    for _ in range(size):
        for i in range(len(t)):
            if len(t[i]) >= 2:
                for j in range(1, len(t[i])):
                    set_true(letters, t[i][j])

        s = reset_map(letters)
        secret = secret + s
        t = remove_letter_from_triplets(t, s)


    return secret


secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

resp = recoverSecret(triplets)
print(resp)