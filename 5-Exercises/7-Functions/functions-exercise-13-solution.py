## Functions. Exercise #13
# Write a function with name "count_multiple_letters". This function
# takes in one argument (a string) and returns a dictionary with
# the keys being the letters and the values being the count of the letter.
# Hint: use a dictionary comprehension and count().
# Expected output:
# count_multiple_letters("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
def count_multiple_letters(word):
    text=word.lower()
    return {letter: text.count(letter) for letter in text}
print(count_multiple_letters("helLo"))
