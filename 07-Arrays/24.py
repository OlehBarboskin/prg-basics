def f(arr):
    entered_value = 7
    number_of_greater = 0
    for i in range(len(arr)):
        if arr[i] > entered_value:
            number_of_greater += 1
    return number_of_greater

array = [3, 8, 12, 5, 20, 1, 7]

print(f(array))  # Output: 3