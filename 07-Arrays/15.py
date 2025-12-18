arr = [2, 9, 1, 5, 6]

def f(arr):
    max_val = 0
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
print (f(arr))

def a(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val
print (a(arr))

def s(arr):
    print(arr)
    sum = 0
    i = 0
    while i < len(arr) + 1:
        sum += arr[i]
        mean = sum / len(arr)
        i += 1
    return mean
print (s(arr))