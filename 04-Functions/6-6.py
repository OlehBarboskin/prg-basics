def is_within_range(number, x, y):
    if x <= number and number <= y:
        return True
    else:
        return False
    
if __name__ == '__main__':
    num = int(input('Enter a number in the range: '))
    x = int(input('Enter the lower limit'))
    y = int(input('Enter the upper limit'))
    print(f'Is the number {num} within the range {x} to {y}? {is_within_range(num, x, y)}')