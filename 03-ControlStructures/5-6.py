N = 10
sum_even = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i

print(f"The sum of even numbers from 1 to {N} is {sum_even}")

N = 10
sum_odd = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        sum_odd += i

print(f"The sum of odd numbers from 1 to {N} is {sum_odd}")