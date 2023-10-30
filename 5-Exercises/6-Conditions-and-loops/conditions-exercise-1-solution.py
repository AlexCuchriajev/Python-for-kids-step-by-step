## Conditions. Exercise #1 solution

import random
choice = random.randint(1, 10)
# We have a code  whuch randomly picks a
# number between 1 and 10, and saves it to
# a variable with name 'choice'.
# Your task is to write a simple conditional
# to check if choice is 7.  If choice  is 7,
# print out "lucky". Otherwise, print out "unlucky".
if choice == 7:
    print("lucky")
else:
    print("unlucky")