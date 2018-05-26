#!/usr/bin/python3

import re

# Opening book and getting list of words

book = open('alice.txt', 'r')

book_words = book.read()

# Getting a clean list of words

clean_words = re.findall(r"[\w']+", book_words)

# Getting sorted list

clean_words = sorted(clean_words)

# Generating word count

word_map = {}

for word in clean_words:
    word_map[word] = 0

for word in clean_words:
    word_map[word] += 1

# Generating output

output = "Word              Count\n" \
         "=======================\n"

keys_list = []

for key in word_map:
    keys_list.append(key)

keys_list = sorted(keys_list)

for key in keys_list:
    output += key.ljust(18) + str(word_map[key]) + '\n'

book.close()

word = open('alice_words.txt', 'w')

word.write(output)
