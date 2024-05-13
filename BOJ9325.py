import sys
input = sys.stdin.readline

s = int(input())
for i in range(s):
    car_price = int(input())
    n = int(input())
    for j in range(n):
        count_option, price = map(int, input().split())
        car_price += count_option*price
    print(car_price)
