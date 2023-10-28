## Lists. Exercise #4 solution:
# Create a list with name 'friends' which will have 5 persons' names.
friends=["Jonas","Petras","Tomas","Vilma","Ona"]
# Add the following names to this list:
    # "Aleksas"
    # "Maksas"
    # "Vladislavas"
friends.append("Aleksas")
friends.append("Maksas")
friends.append("Vladislavas")
#or :
# friends.extend(["Aleksas", "Maksas", "Vladislavas"])
print(friends)

# Remove the last name in this list
friends.pop()
print(friends)

# Remove the first name in this list
friends.pop(0)
print(friends)

# Add the name "Claudia" to the beginning of this list
friends.insert(0,"Claudia")
print(friends)