import math
n, m  = map(int, input().split())
res = math.gcd(n, m)
lcm = math.lcm(n, m)
print(res)
print(lcm)