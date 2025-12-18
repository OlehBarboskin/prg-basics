def f(arr1, arr2):
    if set(arr1) >= set(arr2):
        return True
    return False
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4]
print(f(arr1, arr2))  # Output: True