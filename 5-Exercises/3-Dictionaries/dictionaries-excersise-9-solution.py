## Dictionaries. Exercise #9

# Create a dictionary with the key as a vowel in the alphabet
# and the value as 7.
# Expected output: {'a': 7, 'e': 7, 'i': 7, 'o': 7, '7': 7}.

# Using dict comprehension
answer={char:7 for char in ['a','e','i','o','u']}
print(answer)

answer = {char:7 for char in 'aeiou'}
print(answer)

# Using dict.fromkeys:
answer = dict.fromkeys("aeiou", 7)
print(answer)