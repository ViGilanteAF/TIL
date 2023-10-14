from collections import Counter


def solution(X, Y):
    counter = Counter(X) & Counter(Y)
    if len(counter) == 1 and counter['0'] != 0:
        return '0'
    answer = ''
    for digit in sorted(counter.keys(), reverse=True):
        answer += digit * counter[digit]

    return answer if answer else "-1"
