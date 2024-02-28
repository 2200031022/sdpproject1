import random
import string

def generate_random_color_hex():
    color_hex = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color_hex

def generate_random_alphabetical_string(length):
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_integer_between(start, end):
    random_integer = random.randint(start, end)
    return random_integer

def generate_random_multiple_of_seven():
    random_multiple_of_seven = random.randint(0, 10) * 7
    return random_multiple_of_seven

# Example usages
print("Random Color Hex:", generate_random_color_hex())
print("Random Alphabetical String:", generate_random_alphabetical_string(5))
print("Random Integer between 10 and 20:", generate_random_integer_between(10, 20))
print("Random Multiple of 7 between 0 and 70:", generate_random_multiple_of_seven())