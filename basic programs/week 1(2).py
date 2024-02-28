def get_integer_input():
    while True:
        try:
            user_input = input("Enter an integer value: ")
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

user_integer = get_integer_input()
print("Integer value:", user_integer)
