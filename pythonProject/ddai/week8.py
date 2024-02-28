def mcculloch_pitts(inputs, threshold):

    input_sum = sum(inputs)


    if input_sum >= threshold:
        return 1
    else:
        return 0



def AND_gate(x1, x2):
    inputs = [x1, x2]
    threshold = 2  # For AND gate, threshold is 2
    return mcculloch_pitts(inputs, threshold)


def OR_gate(x1, x2):
    inputs = [x1, x2]
    threshold = 1  # For OR gate, threshold is 1
    return mcculloch_pitts(inputs, threshold)


# Testing AND gate
print("AND Gate:")
print("0 AND 0 =", AND_gate(0, 0))
print("0 AND 1 =", AND_gate(0, 1))
print("1 AND 0 =", AND_gate(1, 0))
print("1 AND 1 =", AND_gate(1, 1))

# Testing OR gate
print("\nOR Gate:")
print("0 OR 0 =", OR_gate(0, 0))
print("0 OR 1 =", OR_gate(0, 1))
print("1 OR 0 =", OR_gate(1, 0))
print("1 OR 1 =", OR_gate(1, 1))
