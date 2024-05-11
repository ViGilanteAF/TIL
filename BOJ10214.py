import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    y_sum = 0
    k_sum = 0
    for j in range(9):

        y, k = map(int, input().split())

        y_sum += y
        k_sum += k

    if y_sum < k_sum:
        print("Korea")
    elif y_sum > k_sum:
        print("Yonsei")
    else:
        print("Draw")
