def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raise an error for division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        # Prompt the user for two numbers
        num1 = float(input("Enter first number: "))  # Convert input to float
        num2 = float(input("Enter second number: "))  # Convert input to float

        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            try:
                result = divide(num1, num2)
                operation = "/"
            except ValueError as e:
                print(e)  # Print error message if division by zero occurs
                return

        # Display the result
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
