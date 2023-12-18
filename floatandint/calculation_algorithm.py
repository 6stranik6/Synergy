number = float(input("Введите пятизначное число: "))
tens = (number // 10) % 10
units = number % 10
power_result = tens ** units
hundreds = (number // 100) % 10
mult_result = power_result * hundreds
tens_thousands = (number // 10000) % 10
thousands = (number // 1000) % 10
diff_result = tens_thousands - thousands
final_result = mult_result / diff_result
print(final_result)