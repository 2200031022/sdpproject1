binary_sequence = input("Enter a sequence of comma separated 4-digit binary numbers: ")
binary_numbers = binary_sequence.split(',')
divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]
print(','.join(divisible_by_5))