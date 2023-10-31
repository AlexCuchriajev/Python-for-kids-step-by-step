## Dictionaries. Exercise #10
# Your task is to create dictionary 'ascii_keys' that maps ASCII keys
# to their corresponding letters.  Use a dictionary comprehension and chr() .
# Save the result to the answer variable.
ascii_keys= {num:chr(num) for num in range(65,91)}
print(ascii_keys)

