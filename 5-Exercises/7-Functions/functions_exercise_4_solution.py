## 7-Functions. Exercise #4 solution:
# Using a list comprehension:
def get_evens():
    return [x for x in range(1,15) if x%2 == 0]

# Using a loop:
def get_evens():
    evens = []
    for x in range(1,15):
        if x % 2 == 0:
            evens.append(x)
    return evens

get_evens()