# There are two lists: [1,2,3,4] and [3,4,5,6],
# Create a new list 'result' which is the intersection of the two lists.
# Expected output: [3,4]
# Hint: use the in  operator to test whether an element is in a list.
# For example:  5 in [1,5,2]  is True.  3 in [1,5,2]  is False.
result = [num for num in [1,2,3,4] if num in [3,4,5,6]]
print(result)

# There is a list of names: ["Alex", "Sam", "Tom"]
# Create a new list 'result' with each word reversed and in lower case
# Expected output: ['xela', 'mas', 'mot']
result = [name.lower()[::-1] for name in ["Alex", "Sam", "Tom"]]
print(result)