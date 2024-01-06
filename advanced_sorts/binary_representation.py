def decimal_to_binary(number):
    if number <= 1:
        return str(number)
    return decimal_to_binary(number // 2) + str(number % 2)
binary_number = decimal_to_binary(13)
print(binary_number)