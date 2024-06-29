n=input()
sum = 10
now = []

for i in range(len(n)):
    n = str(n)
    now.append(n[i])


for i in range(1,len(n)):
    if now[i-1] == n[i]:
        sum += 5
    else: sum += 10

print(sum)