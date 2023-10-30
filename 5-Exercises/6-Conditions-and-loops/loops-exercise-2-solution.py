## Loops. Exercise #2
# Use a for loop to add up every odd number
# from 10 to 20 (inclusive) and store the
# result in the variable 'sum'.
sum=0
for num in range(10,21):
    if num%2!=0:
        sum+=num
print(num)
# or:
for num in range(10,21,2):
    sum+=num
print(num)