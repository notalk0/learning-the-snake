users = ['Ed', 'Homeboi', 'Ana', 'John', 'Snow', 'Betrayed']
print(users[0])

alot_zeros = [0] * 20
print(alot_zeros)

print(users[4:])

# Unpacking
items = ['Laptop', 'Phone', 'Joystick']
laptop, *other = items
print(laptop)
print(other)

# Add Items
users.append('New Item')
users.insert(0, 'Beginning Item')
print(users)

# Remove Items
users.pop()
print(users)

# Tupple
letters = ('a', 'b', 'c', 'd')

# Sets
letters = {'a', 'b', 'c', 'd'}
