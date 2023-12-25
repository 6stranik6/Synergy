def factorial_list(num):
    factorials = []
    for i in range(num, 0, -1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        factorials.append(factorial)
    return factorials
number = int(input("Введите число: "))
result_list = factorial_list(number)
print(result_list)