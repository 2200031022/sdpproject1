def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

try:
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
