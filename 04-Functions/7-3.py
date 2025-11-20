def f(number,even):
    sum = 0
    formated_number = str(number)
    if even is True:
        for char in formated_number:
            if int(char) % 2 == 0:
                sum += int(char)
            else:
                continue
    if even is False:
        for char in formated_number:
            if int(char) % 2 != 0:
                sum += int(char)
            else:
                continue

if __name__ == '__main__':
    print(f(4,True))