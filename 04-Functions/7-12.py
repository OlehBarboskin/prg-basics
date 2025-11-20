def f(n):
    final_string = ''
    n = int(n)
    if n <= 0:
        return ''
    final_string = "/".join(["*"] * n)
    return final_string

if __name__ == '__main__':
    print(f(3))