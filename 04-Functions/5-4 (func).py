def sum_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(f'The sum of the digits in the number {number} is {sum_digits(number)}')