def calculate_average(numbers):
    total = sum(numbers)
    length = len(numbers)
    if length == 0:
        return None
    average = total / length
    return average

numbers_list = [90, 80, 70, 60, 40]
average_result = calculate_average(numbers_list)
print("Average:", average_result)
