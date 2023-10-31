## Loops. Exercise #5 solution
# Create nice art of triangle from "*". Use for and while loops
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# From 1 to 10 (including 10)
# For loop:
image="*"
for row in range(1,11):
    print(image*row)
# While loop:
row=1
while row<11:
    print(image*row)
    row+=1
