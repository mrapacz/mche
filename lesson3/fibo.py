import sys


def fibo_easy(n):
    a, b, c = 1, 1, 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


def fibo_hard(n):
    a, b = 1, 1
    for i in range(2, n):
        b = b + a
        a = b - a
    return b


if __name__ == "__main__":
    fibo = fibo_hard
    print(fibo(int(input("Which Fibonacci number to count?\n"))))
