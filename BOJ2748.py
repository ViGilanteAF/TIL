import sys
input = sys.stdin.readline

n = int(input())
fi = [0]*91
fi[1] = 1
for i in range(2, 92-1):
    fi[i] = fi[i - 2] + fi[i - 1]


print(fi[n])
