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
    return float(num) ** exponent


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return num1 % num2


def my_reduce(function_name, operable_numbers):
    #if function_name == "add":
    i = 0
    for i in range(0, len(operable_numbers)):
        if i == 0:
            partial_result = operable_numbers[0]
        else:
            if function_name == "+":
                partial_result = add(partial_result, operable_numbers[i])
            elif function_name == "-":
                partial_result = subtract(partial_result, operable_numbers[i])
            elif function_name == "*":
                partial_result = multiply(partial_result, operable_numbers[i])
            elif function_name == "/":
                partial_result = divide(partial_result, operable_numbers[i])
            elif function_name == "pow":
                partial_result = power(partial_result, operable_numbers[i])
            elif function_name == "mod":
                partial_result = mod(partial_result, operable_numbers[i])
        i = i + 1
    return "%.2f" % partial_result


# def user_input(new_file):
#     open(new_file)

while True:

    user_input = raw_input("Please input prefix equation: ")

    inputs_list = user_input.split(" ")
    calculation_sign = inputs_list[0]

    if calculation_sign == "q":
        break

    elif calculation_sign == "square" or calculation_sign == "cube":
        if len(inputs_list) == 2:
            try:
                num1 = float(user_input.split(" ")[1])

            except:
                print "Your input is not numerical."
                continue

            if calculation_sign == "square":
                print "%.2f" % square(num1)

            else:
                print "%.2f" % cube(num1)
        else:
            print "Invalid number of arguments."
            continue

    elif calculation_sign in ["+", "-", "*", "/", "pow", "mod"]:
        if len(inputs_list) >= 3:
            try:
                numerical_list = []
                for number in user_input.split(" ")[1:]:
                    number = float(number)
                    numerical_list.append(number)

                #num1 = float(user_input.split(" ")[1])
                #num2 = float(user_input.split(" ")[2])
            except:
                print "Your input is not numerical."
                continue

            if calculation_sign == "+":
                print my_reduce(calculation_sign, numerical_list)

            elif calculation_sign == "-":
                print my_reduce(calculation_sign, numerical_list)

            elif calculation_sign == "*":
                print my_reduce(calculation_sign, numerical_list)

            elif calculation_sign == "/":
                print my_reduce(calculation_sign, numerical_list)

            elif calculation_sign == "pow":
                print my_reduce(calculation_sign, numerical_list)

            elif calculation_sign == "mod":
                print my_reduce(calculation_sign, numerical_list)
        else:
            print "Invalid number of arguments."
            continue

    else:
        print "Sorry we do not support this calculation."
        continue
