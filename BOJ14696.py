import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]

    a_list = [a.count(4), a.count(3), a.count(2), a.count(1)]
    b_list = [b.count(4), b.count(3), b.count(2), b.count(1)]

    for j in range(4):
        if a_list[j] > b_list[j]:
            print("A")
            break
        elif a_list[j] < b_list[j]:
            print("B")
            break
        elif j == 3:
            print("D")
            break