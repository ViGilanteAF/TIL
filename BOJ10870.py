def fib(num):
    # 2. 종료조건
    if num < 2:
        return num

    # 1. 기본동작
    return fib(num - 1) + fib(num - 2)


num = int(input())
print(fib(num))
