def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Welcome to CLI Calculator!")
    print("Supported operations: +, -, *, /")
    while True:
        try:
            expression = input("Enter an expression (or 'q' to quit): ").strip()
            if expression.lower() == 'q':
                break

            operators = {'+', '-', '*', '/'}
            operator = None
            for op in operators:
                if op in expression:
                    operator = op
                    break
            
            if not operator:
                print("Invalid expression. Please try again.")
                continue

            x, y = map(float, expression.split(operator))
            if operator == '+':
                result = add(x, y)
            elif operator == '-':
                result = subtract(x, y)
            elif operator == '*':
                result = multiply(x, y)
            elif operator == '/':
                result = divide(x, y)

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
