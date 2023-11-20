﻿print("Welcome to a simple calculator.")
print("You can only do add (+), subtract (-), division (/), and multiplication (*).")
print("The format must be {number}{space}{operator}{space}{number}. Anything besides that will not work.")
print("Feel free to start:")

while True:
    user_input = input()
    input_list = user_input.split()

    if len(input_list) != 3:
        print("Invalid input format. Please use the format: {number} {operator} {number}")
        continue

    first_number, operator_string, second_number = input_list

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if operator_string == "+":
        result = first_number + second_number
    elif operator_string == "-":
        result = first_number - second_number
    elif operator_string == "*":
        result = first_number * second_number
    elif operator_string == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /")
        continue

    print("Result:", result)
