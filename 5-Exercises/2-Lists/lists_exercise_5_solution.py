## Lists. Exercise 5 solution:

friends = ["Elie", "Tim", "Matt"]
# Create a new list 'friends_letters' containing the first letter of
# each name in the friends list. Use a list comprehension.
friends_letters=[friend[0].upper() for friend in friends]
print(friends_letters)

numbers = [1,2,3,4,5,6]
# Create a new list 'even_numbers' of all the even values.
# Use a list comprehension.
even_numbers=[number for number in numbers if number%2==0]
print(even_numbers)