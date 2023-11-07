'''
문자열 내 마음대로 정렬하기
https://school.programmers.co.kr/learn/courses/30/lessons/12915
연습문제 Lv.1
'''
'''
특정한 기분으로 정렬을 할 경우 lambda식을 사용함
key=lambda x: ()  x 의 경우 strings 의 element 하나하나 라고 보면 됨 
정렬 조건이 여러가지 일 경우 tuple로 묶어주면 됨 => 조건의 높은 우선순위 부터 작성
그래서 최종적으로 key=lambda x : (x[x],x) 로 작성하면 됨

'''


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
