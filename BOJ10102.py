import sys
input = sys.stdin.readline
n = int(input())
data = list(input())
A = B = 0

for i in range(n):
    if data[i] == 'A':
        A += 1
    else:
        B += 1
if A < B:
    print("B")
elif B < A:
    print("A")
else:
    print("Tie")

'''
n = int(input())
d = input() 
a = d.count('A') 
if 2*a> n:
    print('A')
elif 2*a<n:
    print('B')
else:
    print('Tie')
    
'''
