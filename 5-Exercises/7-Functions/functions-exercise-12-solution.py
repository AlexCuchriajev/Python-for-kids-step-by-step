## Functions. Exercise #12
# Write a function with name 'count_single_letter'.
# This function takes in two arguments (two strings).
# The first argument should be a word and the second should be a letter.
# The function returns the number of times that letter
# appears in the word. If the letter is not in the word, the function should return 0.
# Important: The input swould be not dependent on the case
# (can be in lowercase or uppercase.)
# Hint: use count() method
def count_single_letter(word,letter):
    return word.lower().count(letter.lower())
print(count_single_letter("HeLLom","M"))