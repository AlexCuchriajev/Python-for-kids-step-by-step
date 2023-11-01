## Functions. Exercise #9 solution:
# Write a function with name 'day_of_week'. This function takes in one argument
# (a number from 1-7) and returns the day of the week. If the number is
# less than 1 or greater than 7, the function should return "Wrong number. Try again"
# Hint: You can use a list to store the days of the week (or dictionary).

## Using a list
days_of_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
def day_of_week(number):
    if number<1 or number>7:
        return "Wrong number. Try again"
    return days_of_week[number-1]

## Using a dictionary
# days_of_week={k+1:days_of_week[k] for k in range(7)}
# print(days_of_week)
days_of_week={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
def day_of_week(number):
    if number<1 or number>7:
        return "Wrong number. Try again"
    return days_of_week[number]

## With error handling (Extra)
# We have not covered it yet. It eliminates the need to check
# if number is a valid index in the list. We cover this later in the debugging
# section.
def day_of_week(number):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][number-1]
    except IndexError as e:
        return "Wrong number. Try again"

print(day_of_week(5))