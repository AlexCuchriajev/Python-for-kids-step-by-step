## Dictionaries. Exercise #2
# We have a dictionary:
friend = {
    "first_name": "Alex",
    "last_name": "Best",
}
# Declare a variable with name 'full_name' that is equal to
# friend's first and last names with a space between.
# You must reference the values associated with those
# keys in the 'friend' dictionary.
# Expected output: Alex Best

# String concatenation
full_name=friend["first_name"]+" "+friend["last_name"]
print(full_name)

# Using format() method
full_name = "{} {}".format(friend["first_name"], friend["last_name"])
print(full_name)

# Using f string (works in Python 3.6 or greater)
full_name = f"{friend['first_name']} {friend['last_name']}"
print(full_name)