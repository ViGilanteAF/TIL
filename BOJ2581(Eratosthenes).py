'''
에라토스테네스의체
0,1 은 소수 가 아니니 제외
2의 배수, 3의 배수 같이 소수의 배수들을 지워나가며 소수를 찾아내는 방식

'''
m = int(input())
n = int(input())

num = 0

check = [False for i in range(n+1)]
for i in range(2, int(n**(1/2))):
    if check[i] == False:
        for j in range(2 * i, n+1, i):
            check[j] = True
prime_no = []
for i in range(m, n+1):
    if i >= 2:
        if check[i] == False:
            prime_no.append(i)

if len(prime_no) == 0:
    print(-1)
else:
    print(sum(prime_no))
    print(min(prime_no))
