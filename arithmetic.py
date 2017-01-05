def add(num1, num2):
    """Return the sum of two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Return the difference of two numbers"""
    if num1 < num2:
        return num2 - num1
    else:
        return num1 - num2


def multiply(num1, num2):
    """Return the product of two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    if num2 == 0:
        return "The denominator is zero."

    else:
        return float(num1) / num2


def square(num):
    """Return the square of a number"""
    return num * num


def cube(num):
    """Return the cube of a number"""
    return num * num * num


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return float(num) ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2
