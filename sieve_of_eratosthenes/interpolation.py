import random

n = 40
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

to_search = random.randint(1, 100)
answer = -1

arr.sort()
left = 0
right = len(arr) - 1
while(left <= right and
      to_search >= arr[left] and
      to_search <= arr[right]):
    
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]

    index = left + int(part1 * part2)

    if arr[index] == to_search:
        answer = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1

if answer !=-1:
    print(f"Элемент в списке был, уго индекс: {answer}")
else:
    print("Элемента в списке не было")