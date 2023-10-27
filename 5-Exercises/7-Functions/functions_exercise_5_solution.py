## 7-Functions. Exercise #5 solution:
# Good solution
def is_even(num):
    return num % 2 == 0


# Average solution:
def is_even(num):
    if num % 2 == 0:
        return True
    return False


# Bad solution:
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(4))
print(is_even(5))
