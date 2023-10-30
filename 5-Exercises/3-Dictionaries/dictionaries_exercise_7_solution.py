## Dictionaries. Exercise #7
list1 = ["LT", "EU", "UA"]
list2 = ["LITHUANIA", "EUROPE", "UKRAINE"]

# Create a dictionary that looks like this
# {'LT': 'LITHUANIA', 'EU': 'EUROPE', 'UA': 'UKRAINE'}.
# Save it to a variable with name 'abbreviations'.
# Use dictionary comprehension.
abbreviations = {list1[i]:list2[i] for i in range(0,len(list1))}
print(abbreviations)
# Using zip()
abbreviations = dict(zip(list1, list2))
print(abbreviations)