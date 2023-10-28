## Lists. Exercise #9 solution:

# Using a nested list comprehension and range(),
# create a variable called answer  with the following
# expected output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# Hint: use range() to generate the list [0,1,2].
# Repeat 3 times in a nested list comprehension.

answer = [[k for k in range(0,3)] for i in range(0,3)]
print(answer)