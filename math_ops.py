# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        print("Cannot divide by 0")
    else:
        return a / b  # Potential division by zero error


def ultimate_function():
    print("Haha! Prepare to see the ultimate function!")
    print("There is no function superior to me!")
    print("I am not one, not two... but THREE print statements!")

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")
    ultimate_function()