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
        print "The denominator is zero."
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
    return num ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2

# user_input = raw_input("Please input prefix equation: ")
# calculation_sign = user_input.split("")[0]

# if calculation_sign == "square" or calculation_sign == "cube":
#     num1 = user_input.split("")[1]
#     if calculation_sign == "square":
    
#         print square(num1)
#     else: 
#     num1 = user_input.split("")[1]
#     print cube(num1)

# else:
#     num1 = user_input.split("")[1]
#     num2 = user_input.split("")[2]

#     if calculation_sign == "+":   
        
#         print add(num1, num2)

#     elif calculation_sign == "-":

#         print subtract(num1, num2)

#     elif calculation_sign == "*":
        
#         print multiply(num1, num2)
#     elif calculation_sign == "/":
        
#         print divide(num1, num2)


# elif calculation_sign == "pow":
#     num1 = user_input.split("")[1]
#     num2 = user_input.split("")[2]
#     print power(num1, num2)
# elif calculation_sign == "mod":
#     num1 = user_input.split("")[1]
#     num2 = user_input.split("")[2]
#     print mod(num1, num2)
# else:
#     print "Sorry we do not support this calculation."
