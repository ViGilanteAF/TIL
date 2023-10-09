'''
나누어 떨어지는 숫자 배열
https://school.programmers.co.kr/learn/courses/30/lessons/12910
연습문제 Lv.1
'''
# sorted, sort
# lst = [2,3,1,5,4]
# lst2 = sorted(lst)
# lst2 : [1,2,3,4,5]
# lst.sort()
# lst: [1,2,3,4,5]


def solution(arr, divisor):
    answer = [el for el in arr if not el % divisor]
    if not answer:
        return [-1]

    return sorted(answer)
