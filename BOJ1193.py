import sys

input = sys.stdin.readline
'''
n = int(input())
count = 1
x = 1
y = 1
direction = -1
while count < n:
    if x == 1 and direction == -1:
        y += 1
        direction = 1
    elif y == 1 and direction == 1:
        x += 1
        direction = -1
    elif direction == 1:
        x += 1
        y -= 1
    else:
        x -= 1
        y += 1
    count += 1
print(x, '/', y)
'''

n = int(input())
line = 1
while n> line:
    n -= line
    line += 1

if line%2 == 0:
    print(f"{n}/{line + 1 - n}")
else:
    print(f"{line + 1 - n}/{n}")