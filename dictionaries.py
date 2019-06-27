user = {"name": "Ed", "email": "john@yahoo.com",
        "age": 20, "purchases": [1, 2, 3, 4]}

print(user["email"])

user["name"] = 'Anna'

print(user)

for key in user:
    print(key + ':' + str(user[key]))

print(user.keys())
print(user.items())

for key, value in user.items():
    print(value)

if "name" in user:
    print('It is')
