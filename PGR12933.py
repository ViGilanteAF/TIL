'''
정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
연습문제 Lv.1
'''
'''
12345 => [1,2,3,4,5]
divmod(n,10) 를 사용해서 

'''


def solution(n):
    lst = []  # [5, 4, 3, 2, 1]
    while n:  # n = 12345
        n, r = divmod(n, 10)  # n = 1, 2, 3, 4, 5
        lst.append(r)
        lst.sort(reverse=True)
        answer = 0
        for el in lst:  # 54321
            answer *= 10
            answer += el
        return answer
