## Conditions. Exercise #2.
import random

num = random.randint(1, 20)  # picks random number from 1-20
# Use a conditional statement to check if the number
# is odd. If 'num' is odd, print "Number .. is odd", otherwise print "Number .. is even".
# Hint: use modulus %

if num % 2 == 0:
    print(f"Number {num} is even")
else:
    print(f"Number {num} is odd")
