x=int(input("Введите число: "))
i=0

for g in range(1, x+1):
    if x%g==0:
        i=i+1
print(i)