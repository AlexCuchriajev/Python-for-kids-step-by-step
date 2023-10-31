## Dictionaries
person = [["name", "Alex"], ["job", "Python developer"], ["country", "Lithuania"], ["city", "Klaipeda"]]
# Create a dictionary with name 'answer',
# that takes first item in each list as a key and the second item
# as a value. There are many potential solutions for this.
# Expected output: {'name': 'Alex', 'job': 'Python developer', 'country': 'Lithuania','city': 'Klaipeda'}

## Using for loop
answer={}
for item in person:
    answer[item[0]]=item[1]
print(answer)

## Using dictionary comprehension
answer={key:value for key,value in person}
print(answer)

answer = {item[0]: item[1] for item in person}
print(answer)

## Using dict(). If you have a list of pairs,
# you can very easily turn it into a dictionary using dict()
answer=dict(person)
print(answer)