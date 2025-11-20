def f(x,y):
    x,y = int(x), int(y)
    if x > y:
        x,y = y,x
    count = 0
    for n in range(x, y+1):
        if n < 0 and n % 2 == 0:
            count +=1
    return count