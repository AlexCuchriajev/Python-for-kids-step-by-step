## Lists. Exercise #7 solution:
# For all the numbers between 1 and 50 (including 50),
# create a list 'my_list' with all the numbers that are divisible by 12.
# Expected output: [12, 24, 36, 48]
# Use list comprehension
my_list = [num for num in range(1,51) if num%12==0]
print(my_list)