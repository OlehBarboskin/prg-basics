def f(password):
    allowed = False
    if password.count([0]) == 1:
        allowed = True
    if password.count([1]) == 1:
        allowed = True
    if password.count([2]) == 1:
        allowed = True
    if password.count([3]) == 1:
        allowed = True
    if password.count([4]) == 1:
        allowed = True
    if password.count([5]) == 1:
        allowed = True
    if password.count([6]) == 1:
        allowed = True
    if password.count([7]) == 1:
        allowed = True

    if len(password) >= 6 and allowed is True:
        return True
    
print(f("bananana"))