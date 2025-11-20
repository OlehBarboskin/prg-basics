def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    if operator == "*":
        return number1 * number2
    if operator == "%":
        return number1 % number2
    if operator == "**":
        return number1 ** number2
    
if __name__ == '__main__':
    print(f(1,2,'**'))