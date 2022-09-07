def printName(name):
    return f'Hello, my name is {name}!'
print(printName("Nate"))
otherName = printName
print(otherName("Coding Temple"))

# incrementer function
def increase(num):
    return num + 1
#decrementer function
def decrease(num):
    return num - 1

# general operation function 
def operate(func, num):
    res = func(num)
    return res

print(operate(decrease, 10))

# returning another function!
def x():
    def y():
        print('Hello')
    return y

inner = x()
inner()

# may make more sense with context
def x(status):
    def y():
        print('Hello')
    if status:
        return y
    else:
        print('No!')


# Actual decorator
def decorate(func):
    def inner():
        print('I got decorated!')
        func()
    return inner

def undecorated():
    print('You need to buy some art!')

# let's decorate
pretty = decorate(undecorated)
pretty()

# another example
def security(func):
    password = input('Enter creds:')
    if int(password) == 123:
        def inner(password):
            print('Invalid password')
        return inner
    else:
        def inner(password):
            print('Good to go!')
            func(password)
        return inner

        
@security
def setPass(password):
    print('successfully created password!')

setPass(123)
# one way of writing this
# decoratedSetPass = security(setPass, 1234)
# (decoratedSetPass())

