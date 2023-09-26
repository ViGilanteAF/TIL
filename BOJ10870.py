def fib(num):
    return fib(num - 1) + fib(num - 2)


num = int(input())
print(fib(num))
