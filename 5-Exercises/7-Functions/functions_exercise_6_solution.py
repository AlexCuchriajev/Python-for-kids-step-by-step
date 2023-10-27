## 7-Functions. Exercise #6 solution:
# The problem is that the function returns the very first
# time through the loop because of the way return is indented.
# To fix it, all we have to do is outdent the return statement
# so that it now only returns after the loop finishes running
def count_stars(text):
    count = 0
    for char in text:
        if char == '*':
            count += 1
    return count


print(count_stars("*uper *tar *irl"))
