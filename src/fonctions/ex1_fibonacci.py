def fibonacci(n):
    res = None
    if isinstance(n, int) and n >= 0:
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        elif n > 1:
            res = fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("n n'est pas un entier positif")
    return res


if __name__ == "__main__":
    for i in range(10):
        print(fibonacci(i), end=" ")
