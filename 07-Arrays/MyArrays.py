def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2]

def difference(arr):
    max_val = max(arr)
    min_val = min(arr)
    return max_val - min_val

def median(arr):
    n = len(arr)
    median = 0
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2])
    else:
        median = arr[n//2]
    return median

def return_smallest_largest(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest, largest

def return_separated_minus(arr):
    empty_arr = []
    for i in range(len(arr)):
        empty_arr.append(-arr[i])
    return empty_arr
