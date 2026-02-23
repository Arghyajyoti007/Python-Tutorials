# Assignment 12:String Searching and Replacing:
# Given a text containing a sample paragraph of text.
# Write a Python program that reads this paragraph and searches for a “specific word” and display the number of occurrence of that word.
# Replace all occurrences of the word with “replace with” word and display the modified text.

# Given Paragraph: Python is commonly used for developing websites and software, task automation, data analysis, and data visualization.
# Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists,
# for a variety of everyday tasks, like organizing finances

# Specific word: Python
# Replace with : PYTHON

string_input = '''Python is commonly used for developing websites and software, task automation, data analysis, and data visualization.
Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists,
for a variety of everyday tasks, like organizing finances'''

num_occurance = string_input.count("Python")
replace_string = string_input.replace("Python", "PYTHON")
print(f"Number of time 'Python' is there {num_occurance} times")
print(f"Replaced String is {replace_string}")



