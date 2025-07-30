import sys

input = sys.stdin.readline

# 666 1666 2666 3666 4666 5666 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669 

n = int(input())

count = 0
idx = 666

while n > count:
    if '666' in str(idx):
        count += 1

    idx += 1

print(idx - 1)
