from collections import defaultdict, Counter


def solution(my_string):
    letter2count = Counter(my_string)
    answer = []

    for i in range(ord('A'), ord('Z') + 1):
        answer.append(letter2count[chr(i)])
    for i in range(ord('a'), ord('z') + 1):
        answer.append(letter2count[chr(i)])
    return answer
