A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. print the created array.

def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr