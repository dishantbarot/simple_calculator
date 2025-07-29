# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")

    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operator"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
