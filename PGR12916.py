from collections import Counter


def solution(s):
    counter = Counter(s)
    return counter['p'] + counter['P'] == counter['y'] + counter['Y']
