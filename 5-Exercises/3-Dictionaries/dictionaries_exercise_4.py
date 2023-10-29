## Dictionaries. Exercise #4
import random
selection = random.choice(["pizza", "salad","fruit tea","apple pie","coffee"])
# The 'selection' variable stores a randomly chosen menu item like
# "salad" or "tea". Some of these items are in the 'coffee_shop'
# dictionary, and some are not.
coffee_shop = {
    "pizza" : 3,
    "salad": 2,
    "fruit tea": 5,
    "apple pie": 2
}

# Your task is to print out a string depending
# on if food is a value in 'coffee_shop':
# If 'selection' is contained in 'coffee_shop' print out a string
# that states how many items are left: ".. left"
# If 'selection' is not contained in 'coffee_shop',
# print out "We don't have that"
