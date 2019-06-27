def greeting():
    print('Hello there my friend')
    print('What is your name')
    name = input()
    print('Nice to meet you ' + name)


def greeting_name(name):
    print('Hello there ' + name)


def multiply_by_10(number):
    return 10 * number


def add(number, by=1):
    return number + by


# greeting()
greeting_name('Reina')
print(multiply_by_10(21))
print(add(10))
print(add(number=12, by=39))
