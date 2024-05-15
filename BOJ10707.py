import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

a_total = p * a
b_total = b

if p > c:
    b_total += (p-c)*d

print(min(a_total, b_total))
