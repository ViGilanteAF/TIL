'''
정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
연습문제 Lv.1
'''


def solution(n):
    lst = []
    while n:
        n, r = divmod(n, 10)
        lst.append(r)
        lst.sort(reverse=True)
        answer = 0
        for el in lst:
            answer *= 10
            answer += el
        return answer
