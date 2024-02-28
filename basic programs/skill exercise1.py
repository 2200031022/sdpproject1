n = int(input("Enter a Number: "))

if n == 0:
    print("Wrong Input")
else:
    for i in range(n, n + 1):
        val = n * n  # Corrected calculation to find the square
        print( val)
