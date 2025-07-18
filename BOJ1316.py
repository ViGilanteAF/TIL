import sys
input = sys.stdin.readline


n = int(input())
count = 0


for _ in range(n):
    a = input().strip() # 단어입력
    group = True        # 이 단어가 그룹단어인지 판별
    word = set()        # 등장한 문자 저장
    tmp = ''            # 이전 문자 저장
    for j in a:         # 문자 하나씩 반복
        if j != tmp:
            if j in word:   #이전에 등장한 문자가 또 나오면
                group = False
                break
            word.add(j)
        tmp = j
    if group:
        count += 1

print(count)

'''
tmp 와 set으로 배열를 만들어서 나눠담고 비교해서 걸리면 그룹단어 제외
안걸리면 그룹단어 임
'''