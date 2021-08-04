try:
    number1 = int(input("Enter number 1"))
    operator = input("ENTER operator + - * /")
    number2 = int(input("Enter number 2"))

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    else:
        print("Please enter correct operator")
except ValueError:
    print("Enter number only")
except ZeroDivisionError:
    print("Cannot do number zero")
