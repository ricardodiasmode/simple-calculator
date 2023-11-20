import calculatorOperator
import inputGetter

print("Welcome to a simple calculator.")
print("You can only do add (+), subtract (-), division (/), and multiplication (*).")
print("The format must be {number}{space}{operator}{space}{number}. Anything besides that will not work.")
print("Feel free to start:")

while True:

    first_number, operator_string, second_number = inputGetter.get_user_input()
    if first_number is None:
        continue

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    result = calculatorOperator.operation(first_number, second_number, operator_string)
    if result is None:
        continue

    print("Result:", result)
