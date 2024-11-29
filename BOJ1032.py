import sys
input = sys.stdin.readline

n = int(input())
text = []
for i in range(n):
    text.append(input())

ans = list(text[0])

for i in range(1, len(text), 1):
    for j in range(0, len(text[0]), 1):
        if text[0][j] != text[i][j]:
            ans[j] = "?"

for it in ans:
    print(it, end='')
