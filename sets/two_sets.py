numbers1 = set()
n1 = int(input())
for _ in range(n1):
    num = int(input())
    numbers1.add(num)

numbers2 = set()
n2 = int(input())
for _ in range(n2):
    num = int(input())
    numbers2.add(num)

intersection = numbers1 & numbers2
print(len(intersection))