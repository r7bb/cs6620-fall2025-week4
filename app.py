"""Simple calculator module with basic arithmetic operations."""


def add(num1, num2):
    """Add two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract two numbers."""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Divide two numbers."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def calculate(operation, num1, num2):
    """Perform calculation based on operation."""
    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    return result


def main():
    """Run a short demo of the calculator."""
    print("Simple Calculator")
    print("-" * 20)

    result1 = calculate('add', 10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calculate('multiply', 7, 3)
    print(f"7 * 3 = {result2}")

    print("Calculator completed successfully!")


if __name__ == "__main__":
    main()
