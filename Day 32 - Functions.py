print("")


def abc():
    print("Hello World")  # simple function


abc()

print("")


def calloutFun(a, b):  # to passout 2 variables
    print(a+b)


calloutFun(20, 10)

print("")


def alreadydefined(a, b=10):  # predefined function
    print(a+b)


alreadydefined(10)
print("")


def returnfun(i, j):  # return function
    x = i + j
    return x


output = returnfun(25, 75)
print(output)
