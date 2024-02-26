def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1,2,3,4,5) or (+,-,*,/): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ("1","2","3","4") or choice in ("+","-","*","/"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        if choice == "1" or choice == "+":
            result = addition(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == "2" or choice == "-":
            result = subtraction(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == "3" or choice == "*":
            result = multiplication(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == "4" or choice == ":" or choice == "/":
            result = division(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice.")
