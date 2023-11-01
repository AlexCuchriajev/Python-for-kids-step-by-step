## Functions. Exercise #11 solution:

# Write a function with name 'compare'.
# This function takes in two arguments (both numbers), finds the maximum and
# returns ".. is higher". If numbers are equal - returns "Numbers are equal"
'''
compare(1,1) # "Numbers are equal"
compare(1,0) # "1 is higher"
compare(2,3) # "3 is higher"
'''
def compare(num1,num2):
    max=None
    if num1 > num2:
        max=num1
    elif num2 > num1:
        max=num2
    else:
        return "Numbers are equal"
    return f"{max} is higher"
## Using max() function
# def compare(num1,num2):
#     if num1==num2:
#         return "Numbers are equal"
#     return f"{max(num1,num2)} is higher"

print(compare(1,1))
print(compare(1,0))
print(compare(2,3))