'''
문자열 내 마음대로 정렬하기
https://school.programmers.co.kr/learn/courses/30/lessons/12915
연습문제 Lv.1
'''


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
