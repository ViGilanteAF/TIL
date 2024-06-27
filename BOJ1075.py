n = int(input())
f = int(input())

n = int(n/100)
n = int(n*100)

while(True):
    if(n%f==0):
        break
    else: n= n+1

print(str(n)[-2:])