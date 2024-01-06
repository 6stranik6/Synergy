def multiplication(x, y):
    if y == 0:
        return 0
    return x + multiplication(x, y - 1)
result = multiplication(5, 3)
print(result)