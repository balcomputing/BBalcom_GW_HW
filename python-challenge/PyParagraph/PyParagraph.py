# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "paragraph_1.txt")
file_to_output = os.path.join("paragraph_analysis.txt")

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
print(word_split)
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    words_per_sentence.append(word_split)

# Calculate the avg word count (per sentence)
#YOUR CODE HERE
    
# Generate Paragraph Analysis Output
#YOUR CODE HERE

# Print all of the results (to terminal)
#YOUR CODE HERE
    
# Save the results to analysis text file
#YOUR CODE HERE
