firstnumber = int(input("write first number: "))
secondnumber = int(input("write second number: "))
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
    result = firstnumber+secondnumber
    print(result)
def divide():
    result = firstnumber/secondnumber
    print(result)
def minus():
    result = firstnumber-secondnumber
    print(result)
def multiply():
    result = firstnumber*secondnumber
    print(result)
main()