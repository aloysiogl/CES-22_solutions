#!/usr/bin/python3


def cleanword(string):
    """This function removes non anu of a string"""

    newString = ""

    for char in string:
        if char.isalnum():
            newString += char

    return newString


def has_dashdash(string):
    """This function detects if a word was two dashes"""

    if string.find("--") == -1:
        return False

    return True


def extract_words(string):
    """This function extracts only the words in a string"""

    listWords = []

    toAdd = ""

    for char in string:
        if char.isalnum():
            toAdd += char
            # print(toAdd)
        else:
            if len(toAdd) > 0:
                listWords += [toAdd.lower()]
                toAdd = ""

    if len(toAdd) > 0:
        listWords += [toAdd.lower()]

    return listWords


def wordcount(word, listWords):
    """This function counts the number of occurences of a given word in a list of words"""

    counter = 0

    for wd in listWords:
        if wd == word:
            counter += 1

    return counter


def wordset(wordsList):
    """This function generates a word set from a word list"""

    set = []

    for wd in wordsList:
        if wd not in set:
            set.append(wd)

    set = sorted(set)

    return set


def longestword(wordsList):
    """This function finds the longest word in a list of words"""

    longest = 0

    for wd in wordsList:
        if len(wd) > longest:
            longest = len(wd)

    return longest
