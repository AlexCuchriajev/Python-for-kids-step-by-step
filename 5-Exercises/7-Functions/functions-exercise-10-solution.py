# Functions. Exercise #10 solution:
# Write a function with name 'get_last'. This function takes in one argument
# (a list) and returns the last value in the list. It should return None if
# the list is empty.
# Expected output:
'''
get_last([2,4,5]) -> 5
get_last([])      -> None
'''

# def get_last(l):
#     if l:
#         return l[len(l)-1]
# or:
def get_last(l):
    if l:
        return l[-1]
print(get_last([1,2,5]))
print(get_last([]))