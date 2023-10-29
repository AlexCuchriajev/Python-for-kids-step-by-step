## Dictionaries. Exercise #4 solution
import random
selection = random.choice(["pizza", "caesar salad","fruit tea","apple pie","coffee"])
# The 'selection' variable stores a randomly chosen menu item like
# "salad" or "tea". Some of these items are in the 'coffee_shop'
# dictionary, and some are not.
coffee_shop = {
    "pizza" : 3,
    "caesar salad": 2,
    "fruit tea": 5,
    "apple pie": 2
}

# Your task is to print out a string depending
# on if food is a value in 'coffee_shop':
# If 'selection' is contained in 'coffee_shop' print out a string
# that states how many items are left: "fruit tea: 5 left"
# If 'selection' is not contained in 'coffee_shop',
# print out "coffee : we don't have that"
if selection in coffee_shop:
    print(f"{selection} : {coffee_shop[selection]} left")
else:
    print(f"{selection} : we don't have that")

# Using get()
quantity = coffee_shop.get(selection)
if quantity:
    print(f"{selection} : {quantity} left")
else:
    print(f"{selection} : we don't have that")