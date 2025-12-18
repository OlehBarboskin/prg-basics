def occurs(number,array):
    if number in array:
        return True
    return False

arr = [10, 20, 30, 40, 50]
num = 29
print(occurs(num, arr))  # Output: True