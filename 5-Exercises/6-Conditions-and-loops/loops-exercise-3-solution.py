## Loops. Exercise #3 solution
# User enters number and message printed in console same amount of times.
# For example, user enters 3 and message printed 3 times
user_input = int(input("How many times? "))
for _ in range(user_input):
    print("HELLO!!!")
# or:
print("HELLO!!!\n"*user_input)