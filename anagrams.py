#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function, find_anagrams(), which can be used to do the same
for an arbitrary list of strings.
"""

__author__ = "aradcliff"

import sys


def alphabetize(string):
    """Returns alphabetized version of the string."""
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = {}
    for word in words:
        key = alphabetize(word)
        if key in anagrams:
            anagrams[key].append(word)
        anagrams[key] = [word]
    return anagrams

    # anagrams = {
    #     alphabetize(word): [
    #         w for w in words
    #         if alphabetize(w) == alphabetize(word)]
    #     for word in words}
    # return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print(f"{k} : {v}")


if __name__ == "__main__":
    main(sys.argv[1:])
