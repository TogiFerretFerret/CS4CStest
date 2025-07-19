# High-powered native python calculator

def main():
    """
    Main function to run the calculator.
    """
    print("Welcome to the MeowingSim Calculator!")
    print("Enter 'quit' to exit.")

    while True:
        try:
            expression = input(">>> ")
            if expression.lower() == 'quit':
                break
            result = evaluate(expression)
            print(result)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break


import decimal

def evaluate(expression):
    """
    Evaluates the given mathematical expression.
    """
    try:
        # Set precision for decimal calculations
        decimal.getcontext().prec = 50
        # Evaluate the expression using decimal objects
        result = eval(expression, {"__builtins__": None}, {"Decimal": decimal.Decimal})
        return result
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    main()
