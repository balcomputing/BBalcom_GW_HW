# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string
from collections import Counter

# Paths
resume_path = os.path.join("resume.md")

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation

# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)


# Clean Punctuation

word_list = [''.join(c for c in word_set if c not in string.punctuation) for word_set in word_list]

word_set = set(word_list)

# Clean Stop Words
stop_words = set(["and", "with", "using", "##", "working", "in", "to"])
cleaned_words = word_set - stop_words
#cleaned_words = word_list - stop_words

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1

# Using collections.Counter
word_counter = Counter(word_list)

# Comparing both word count solutions
#print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")


# Sort words by count and print the top 10
sorted_words = []
for word in sorted(cleaned_words, key=word_count.get, reverse=True)[:10]:
    print(f"Token: {word:20} Count: {word_count[word]}")
