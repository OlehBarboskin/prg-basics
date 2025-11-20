def is_binary_number(s):
    for char in s:
        if char not in '01':
            return False
    return True

if __name__ == '__main__':
    binary_string = input('Enter a binary number: ')
    print(is_binary_number(binary_string))