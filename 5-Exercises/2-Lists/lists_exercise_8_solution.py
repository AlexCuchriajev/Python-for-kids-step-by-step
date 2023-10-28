## Lists. Exercises #8 solution:
# Create a list "my_list" containing all
# # the letters from "beautiful" but not the vowels
# (a, e, i, o, and u).
# Expected output: ['b', 't', 'f', 'l'].
# Use a list comprehension

# Using a string:
my_list = [char for char in "beautiful" if char not in "aeiou"]

# Using a list:
my_list = [char for char in "beautiful" if char not in ["a", "e", "i", "o", "u"]]

print(my_list)