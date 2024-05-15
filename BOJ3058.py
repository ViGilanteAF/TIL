import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a = list(map(int, input().split()))
    sum = 0
    min_val = 101
    for j in range(len(a)):
        if a[j] % 2 == 0:  # 짝수일때
            sum += a[j]      # 합
            if min_val > a[j]:  # 최소값 갱신
                min_val = a[j]

    print(str(sum) + " " + str(min_val))
