## 7-Functions. Exercise #3 solution:
# Using string concatenation:
def change_to_upper(text):
    return text.upper()

# Using the string format() method:
def change_to_upper(text):
    return "{}".format(text.upper())

# Using an f-string, (works in Python 3.6 or later):
def change_to_upper(text):
    return f"{text.upper()}"

print(change_to_upper("hello"))