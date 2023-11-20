
def get_user_input():
    user_input = input()
    input_list = user_input.split()

    if len(input_list) != 3:
        print("Invalid input format. Please use the format: {number} {operator} {number}")
        return None, None, None

    return input_list
