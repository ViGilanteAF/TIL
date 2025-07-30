import sys

input = sys.stdin.readline

m = []
s = []

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    m.append([x, y])

for k in range(len(m)):
    count = 1
    for j in range(len(m)):
        # 자기 자신은 제외 하고 같은 자리 끼리 비교 해서 카운트를 증가 시켜준뒤 증가된 값을 s배열에 저장
        if k != j and m[k][0] < m[j][0] and m[k][1] < m[j][1]:
            count += 1
    s.append(count)
#배열에 들어있는 값을 공백으로 구분하여 출력할때 사용
print(' '.join(map(str, s)))

