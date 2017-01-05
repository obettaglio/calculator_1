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
            elif function_name == "/" and isinstance(partial_result, float):
                partial_result = divide(partial_result, operable_numbers[i])
            elif function_name == "pow":
                partial_result = power(partial_result, operable_numbers[i])
            elif function_name == "mod":
                partial_result = mod(partial_result, operable_numbers[i])
            else:
                return "The denominator is zero."
        i = i + 1
    return "%.2f" % partial_result


def calculator_rules(user_input):

    while True:

        #user_input = raw_input("Please input prefix equation: ")

        inputs_list = user_input.split(" ")
        calculation_sign = inputs_list[0]

        if calculation_sign == "q":
            return "Quit"
            break

        elif calculation_sign == "square" or calculation_sign == "cube":
            if len(inputs_list) == 2:
                try:
                    num1 = float(user_input.split(" ")[1])

                except:
                    return "Your input is not numerical."
                    break

                if calculation_sign == "square":
                    return "%.2f" % square(num1)

                else:
                    return "%.2f" % cube(num1)
                break

            else:
                return "Invalid number of arguments."
                break

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
                    return "Your input is not numerical."
                    break

                if calculation_sign == "+":
                    return my_reduce(calculation_sign, numerical_list)

                elif calculation_sign == "-":
                    return my_reduce(calculation_sign, numerical_list)

                elif calculation_sign == "*":
                    return my_reduce(calculation_sign, numerical_list)

                elif calculation_sign == "/":
                    return my_reduce(calculation_sign, numerical_list)

                elif calculation_sign == "pow":
                    return my_reduce(calculation_sign, numerical_list)

                elif calculation_sign == "mod":
                    return my_reduce(calculation_sign, numerical_list)

                break
            else:
                return "Invalid number of arguments."
                break

        else:
            return "Sorry we do not support this calculation."
            break


def user_input():
    the_file = open("operation_command.txt")
    for line in the_file:
        line = line.rstrip()
        print calculator_rules(line)

user_input()
