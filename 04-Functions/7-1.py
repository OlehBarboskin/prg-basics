def f(amount_to_pay):
    coins = 0
    coins += amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5
    coins += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    coins += amount_to_pay
    return coins

if __name__ == '__main__':
    print(f(8))