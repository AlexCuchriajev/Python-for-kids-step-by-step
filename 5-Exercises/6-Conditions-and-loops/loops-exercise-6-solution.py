## Loops. Exercise #6 solution:

# Write a while loop to keep generating a new random 'number'
# between 1 and 10 using random.randint(1, 10), while the
# random number is not equal to 5.
# Every time the loop runs, increment the variable i.

import random
number = 0
i = 0
while number!=5:
    i+=1
    number = random.randint(1, 10)
    print(i,number)