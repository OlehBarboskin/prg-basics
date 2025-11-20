def f(detector):
    counter = 0
    for i in detector:
        if i == '+':
            counter += 1
    if counter >= 3:
        return True
    else:
        return False

if __name__ == '__main__':
    print(f("+--+---"))