def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
