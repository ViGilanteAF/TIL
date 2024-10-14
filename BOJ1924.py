import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n = 0
mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for i in range(a):
    n += mon[i]

n += b
print(day[n%7])