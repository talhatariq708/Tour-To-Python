print('''
    Adding "+"
    Subtracting "-"
    Multiplication "*"
    Division "/"
''')
num_1 = int(input("Enter your Number1:- "))
num_2 = int(input("Enter your Number2:- "))
opr = input("Enter the operator (+ , - , * , / , %) ")
if opr == "+":
    print(num_1 + num_2)
elif opr == "-":
    print(num_1 - num_2)
elif opr == "*":
    print(num_1 * num_2)
elif opr == "/":
    print(num_1 / num_2)
elif opr == "%":
    print(num_1 % num_2)
else:
    print("Invalid Operator")
