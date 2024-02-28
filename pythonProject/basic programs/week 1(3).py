def add_complex(complex1, complex2):
    return complex1 + complex2

def add_float(float1, float2):
    return float1 + float2

def add_integer(int1, int2):
    return int1 + int2

complex_number1 = 5 + 5j
complex_number2 = 4 + 7j
result_complex = add_complex(complex_number1, complex_number2)
print("Sum of complex numbers:", result_complex)

float_number1 = 1.43
float_number2 = 2.632
result_float = add_float(float_number1, float_number2)
print("Sum of float numbers:", result_float)

integer_number1 = 20
integer_number2 = 4
result_integer = add_integer(integer_number1, integer_number2)
print("Sum of integer numbers:", result_integer)
