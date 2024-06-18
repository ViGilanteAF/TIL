count = 0
for i in range(8):
    con = input()
    for j in range(8):
        if (con[j] == 'F' and (i+j) % 2 == 0):
            count += 1


print(count)

'''
0,0 부분이 흰색이고 0,1 이 검은색 0,2 가 흰색 으로 흰색은 i 와 j 가 모두 짝수 인 좌표에만 존재하게 된다.
그러고 그부분에 말 이 있으면 갯수를 저장해주면 된다.
'''
