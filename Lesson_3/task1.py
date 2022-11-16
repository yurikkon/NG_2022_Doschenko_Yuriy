def main():
    operation = input("What operation?")
    if operation == "-":
        minus()
    if operation == "+":
        plus()
    if operation == "*":
        multiply()
    if operation == "/":
        divide()
def plus():
    a = int(input("write first number: "))
    b = int(input("write second number: "))
    result = a+b
    print(result)
def divide():
    a = int(input("write first number: "))
    b = int(input("write second number: "))
    result = a/b
    print(result)
def minus():
    a = int(input("write first number: "))
    b = int(input("write second number: "))
    result = a-b
    print(result)
def multiply():
    a = int(input("write first number: "))
    b = int(input("write second number: "))
    result = a*b
    print(result)
main()