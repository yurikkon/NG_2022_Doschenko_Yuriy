firstnumber = int(input("write first number: "))
secondnumber = int(input("write second number: "))
operation = input("What operation?")
def main():
    if operation == "-":
        return minus()
    if operation == "+":
        return plus()
    if operation == "*":
        return multiply()
    if operation == "/":
        return divide()

def plus():
    return firstnumber+secondnumber

def divide():
    return firstnumber/secondnumber

def minus():
    return firstnumber-secondnumber

def multiply():
    return firstnumber*secondnumber

if operation == "+":
    resultplus = plus()
    print(resultplus)

if operation == "-":
    resultminus = minus()
    print(resultminus)

if operation == "*":
    resultmultiply = multiply()
    print(resultmultiply)

if operation == "/":
    resultdivide = divide()
    print(resultdivide)

main()