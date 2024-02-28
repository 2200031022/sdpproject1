input("enter a number")
x = 0
str1 = "***"
for i in str1:
    x = x + 1
    print(str1[0:x])
num_stars = int(input("Enter the number of stars: "))

for i in range(num_stars):
    print('*' * (i + 1))

input("enter a number")  # Fixed indentation here
x = 0
str2 = "***"
for i in str2:
    x = x + 1
    print(str2[0:x])
    num_stars = int(input("Enter the number of stars: "))

    for i in range(num_stars):
        print('*' * (i + 1))

