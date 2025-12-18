a = [4, 36, 12, 28, 9, 44, 5]
b = [5, 1, 36]

result = []
for x in a:
    if x not in set(b):
        result.append(x)
print(result)  # prints: 4 12 28 9 44