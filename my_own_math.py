my_favourite_no = 3732

def intro():
    print("This is my own math module.")
    print(f"My favourite number is {my_favourite_no}. Dont know why? leave it to me.")

def add(x, y):
    """Returns the sum of x and y.""" # just a docstring to explain the function.
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y    

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    """Returns x raised to the power of y."""
    return x ** y

