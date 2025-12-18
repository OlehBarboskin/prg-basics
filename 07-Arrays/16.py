arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = arr[0]
for i in range(len(arr)):
    if len(arr[i]) > len(longest_name):
        longest_name = arr[i]
print("The longest name is:", longest_name)

n = [2, 6, 4, 9, 7]

def star(n):
    for i in range(len(n)):
        print('*' * n[i])

star(n)