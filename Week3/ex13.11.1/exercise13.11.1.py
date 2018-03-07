#!/usr/bin/python3

# File to open

file = open("text.txt", "r")

# Getting the list of lines

lines = file.readlines()

file.close()

# Reverting the list of lines

lines = reversed(lines)

# Opening new file

output = open("output.txt", "w")

# Writing the new files

for line in lines:
    output.write(line)
