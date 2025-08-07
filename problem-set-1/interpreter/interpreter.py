import operator


def interpreter():
    expression = input("Expression: ").split(" ")

    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    if y == "+":
        y = operator.add
    elif y == "-":
        y = operator.sub
    elif y == "/":
        y = operator.truediv
    else:
        y = operator.mul

    result = float(y(x, z))
    print(result)



interpreter()
