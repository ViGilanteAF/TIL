import sys
input = sys.stdin.readline

n = int(input())
m = input()
cnt = 1
lcheck = 0

for i in m:
   if i == 'S':
       cnt += 1
   elif i == 'L':
       if lcheck == 1:
           cnt += 1
           lcheck = 0
       else:
           lcheck += 1

print(min(cnt,n))

# s = m.count('S') + m.count('LL') + 1
# print(min(s, n))