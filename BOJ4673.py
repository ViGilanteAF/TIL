s = set()  # 생성자 자신을 더하는 로직
for i in range(1, 10001):
    s.add(i+sum(int(x) for x in str(i)))
for j in range(1, 10001):
    if j not in s:
        print(j)