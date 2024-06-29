# while True:
#     try:
#         n = str(input())
#         s = 0
#         d = 0
#         u = 0
#         e = 0
#         for i in range(len(n)):
#             if n[i] == ' ':
#                 s +=1
#             elif n[i] >= 'a' and n[i] <= 'z':
#                 d +=1
#             elif n[i] >= 'A' and n[i] <= 'Z':
#                 u +=1
#             else: e +=1
#         print(d,u,e,s)
#     except EOFError:
#         break

import sys
while True:
    #readline() 로 입력을 받고 바로 .rstrip('\n') 을 이용해서 줄바꿈을 해준다.
    n = sys.stdin.readline().rstrip('\n')
    #그런뒤 if not을 이용하여 간단하게 예외처리를 해준다. 만약 n에 입력값이 없을경우 break!
    if not n:
        break
    s = 0
    d = 0
    u = 0
    e = 0
    for i in range(len(n)):
        if n[i].isspace():
            s +=1
        elif n[i].islower():
            d +=1
        elif n[i].isupper():
            u +=1
        elif n[i].isdigit():
            e +=1
    print(d,u,e,s)
