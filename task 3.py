def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

print("Welcome to Basic Calculator.")

again = True
while again:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter the operator (+, -, *, /): ").strip()

    if choice in ('+', '-', '*', '/'):
        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

    user_choice = input("Enter 'yes' or 'y' to perform operation again: ").strip().lower()
    if user_choice != 'y' and user_choice != 'yes':
        again = False
        print("Thanks for using this program.")
