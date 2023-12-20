m = int(input("Ввидите максимальную массу, которую может выдержать одна лодка "))
n = int(input("Ввидите количество рыбаков, а полсе вес каждого рыбака "))
weights = []

for i in range(n):
    weights.append(int(input()))
weights.sort()
min_boats = 1
for i in range(len(weights) - 1):
    if weights[i] + weights[i+1] <= m:
        min_boats += 1
print(min_boats)