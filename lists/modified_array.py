n = int(input())

numbers = list(map(int, input().split()))
for i in range(n // 2):
    numbers.insert(0, numbers.pop())
print(' '.join(map(str, numbers)))