from arithmetic import *
"""Import operation functions from 'arithmetic.py'."""


def my_reduce(function_name, operable_numbers):
    """Perform operation on multiple inputs."""

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


result = []


def calculator_rules(user_input):
    """Define desired operation, perform, and append result to list."""

    while True:

        #user_input = raw_input("Please input prefix equation: ")

        inputs_list = user_input.split(" ")
        calculation_sign = inputs_list[0]

        if calculation_sign == "q":
            result.append("Quit")

        elif calculation_sign == "square" or calculation_sign == "cube":
            if len(inputs_list) == 2:
                try:
                    num1 = float(user_input.split(" ")[1])

                except:
                    result.append("Your input is not numerical.")
                    break

                if calculation_sign == "square":
                    result.append("%.2f" % square(num1))

                else:
                    result.append("%.2f" % cube(num1))

            else:
                result.append("Invalid number of arguments.")

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
                    result.append("Your input is not numerical.")
                    break

                result.append(my_reduce(calculation_sign, numerical_list))
            else:
                result.append("Invalid number of arguments.")

        else:
            result.append("Sorry we do not support this calculation.")
        break


def user_input():
    """Read input from a file."""

    the_file = open("operation_command.txt")
    for line in the_file:
        line = line.rstrip()
        calculator_rules(line)


result_holder = user_input()

with open('result.txt', 'w') as new_file:
    """Save results to 'result.txt'."""

    for r in result:
        new_file.write("%s\n" % r)
