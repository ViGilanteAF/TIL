from collections import defaultdict


def solution(name, yearning, photo):
    name2yearning = defaultdict(int)

    for n, y in zip(name, yearning):
        name2yearning[n] = y
    answer = []
    for p in photo:
        # score = 0
        # for name in p:
        score = sum(name2yearning[name] for name in p)
        # if name in name2yearning:
        #     score += name2yearning[name]
        answer.append(score)
    return answer

# 1. name 이랑 yearning 이 1:1 로 맵핑 -> name2yearning
