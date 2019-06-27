language = 'Python'
print(len(language))

# Access each individual
print(language[1])
print(language[0:3])
print(language[1:])
print(language[:4])
print(language[-1])

# String Methods
print(language.upper())

street = 'Street Of The DEAD WHITE WALKERS RIP 1 EPISODE'
lower_text = street.lower()
print(lower_text)

print(street.find('dead'))
print(street.find('DEAD'))

lower_text = street.replace("WHITE", "Dead Story Line")
print(lower_text)
