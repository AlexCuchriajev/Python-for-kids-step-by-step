## Dictionaries. Exercise #3 solution

friends_ages = {"alex":21, "sam": 20, "max":23, "tom":22}
# Use a loop to calculate the average of the friends' ages.
# Save the result to a variable with name 'average'.
# Expected output: 21.5
total=0
for age in friends_ages.values():
    total+=age
average=total/len(friends_ages.values())
print(average)

# Using a built-in function called sum()

total = sum(age for age in friends_ages.values())
average=total/len(friends_ages.values())
print(average)

# Using a built-in function called sum()
total = sum(friends_ages.values())
average=total/len(friends_ages.values())
print(average)