def f(arr):
    empty_array = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            empty_array.append(arr[i])
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            empty_array.append(arr[i])
    return empty_array
array = [7,9,2,4,5,6]
print(f(array))  # Output: [2, 8, 4, 6, 5, 3, 1, 7]

