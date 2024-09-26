import math

n = int(input())

if n > 1:
    for i in range(2, int(math.sqrt(n))+1,1): # int(n**(0.5))+1
        while n % i == 0:
            print(i)
            n = n/i # n //= i

    if(n>1):
        print(int(n))

