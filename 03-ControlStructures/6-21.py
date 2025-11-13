enter_money = int(input("Enter the amount of money: "))

print(f'The amount of money {enter_money}')

five_pln_coins = enter_money // 5
two_pln_coins = (enter_money % 5) // 2
one_pln_coins = enter_money - (five_pln_coins * 5 + two_pln_coins * 2)

print(f'Coins of 5 PLN: {five_pln_coins}\nCoins of 2 PLN: {two_pln_coins}\nCoins of 1 PLN: {one_pln_coins}')