numbers = input("Введите последовательность чисел через пробел: ").split()

unique_numbers = set()

for number in numbers:
    if number in unique_numbers:
        print("YES")
    else:
        print("NO")
        unique_numbers.add(number)