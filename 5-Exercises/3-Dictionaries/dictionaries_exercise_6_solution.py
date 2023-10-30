## Dictionaries. Exercise #6 solution
address_book = {'name': "Alex", 'phone': +370634393738}
# 1. Make a copy of 'address_book' and save it to a variable with name
# 'my_list' using a dictionary method.
my_list = address_book.copy()
print(my_list)
# 2. Add the value 32 to my_list under the key "age"
my_list["age"]=32
print(my_list)
# 3. Remove 'age' from my_list using a dictionary method.
my_list.pop("age")
print(my_list)