N = int(input("Введите число N: "))
zero_count = 0

for _ in range(N):
    num = int(input("Введите целое число: "))
    if num == 0:
        zero_count += 1
print("Количество нулевых чисел:", zero_count)