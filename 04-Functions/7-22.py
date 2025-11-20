def f(name):
    parts = name.split()
    return "".join(p[0] for p in parts)

other = "huh huh"
some = other.split()
if __name__ == "__main__":
    print(some)
    print(f("Internet of Things"))