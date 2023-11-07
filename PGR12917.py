'''
문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
연습문제 Lv.1
'''

'''
리스트가 아닌 문자열(String) 또한 sorted 에 넣어줄 수 있음
그러나 반환은 무조건 list 형태로 반환이 되기 때문에 
String 으로 합쳐줘야 함
.join 을 사용하면 됨
'''


def solution(s):
    return ''.join(sorted(s, reverse=True))
