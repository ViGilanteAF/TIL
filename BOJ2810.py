import sys
input = sys.stdin.readline

n = int(input())
m = list(map(str,input()))
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