'''
문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
연습문제 Lv.1
'''


def solution(s):
    return ''.join(sorted(s, reverse=True))
