def sum(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiplication(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return first_number / second_number


def operation(first_number, second_number, operator_as_string):
    if operator_as_string == "+":
        return sum(first_number, second_number)
    elif operator_as_string == "-":
        return subtraction(first_number, second_number)
    elif operator_as_string == "*":
        return multiplication(first_number, second_number)
    elif operator_as_string == "/":
        return division(first_number, second_number)
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /")
        return None
