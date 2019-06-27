# For loop
users = ['Ed', 'Ana', 'John', 'Podrick', 'Smith']

for user in users:
    print('Hello there user')
    print(user)

name = list('Edwin')
print(name)

my_list = list(range(0, 10))
print(my_list)

my_list = list(range(0, 101, 5))
print(my_list)

for i in range(0, 20):
    print('I RUN 20 TIMES')

name = 'Edmin'
for letter in name:
    print(letter)

# While Loop
age = 0
while age <= 20:
    age += 1
    if age == 14:
        continue
        # break
    print(age)
