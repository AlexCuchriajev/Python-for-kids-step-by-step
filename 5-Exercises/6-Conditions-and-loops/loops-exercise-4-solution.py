## Loops. Exercise #4 solution
# Loop through numbers from 1 to 20 (including 20)
# If number is 4 or 13, print out ".. is unlucky"
# If even numbers, print out ".. is even"
# If odd numbers, print out ".. is odd"
for number in range(1,21):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    if number == 4 or number == 13:
        print(f"{number} is unlucky")