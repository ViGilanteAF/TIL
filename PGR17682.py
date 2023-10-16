# 점수 0 - 10 | 보너스 S, D, T  | [옵션] *, #
def solution(dartResult):
    idx = 0
    scores = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    while idx < len(dartResult):
        score = 0
        while dartResult[idx].isdigit():
            score *= 10
            score += int(dartResult[idx])
            idx += 1
        score = score ** bonus[dartResult[idx]]
        idx += 1
        scores.append(score)
        if idx < len(dartResult) and dartResult[idx] == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
            idx += 1
        elif idx < len(dartResult) and dartResult[idx] == '#':
            scores[-1] *= -1
            idx += 1
    return sum(scores)


# "1234" -> 1234, int("1234")


def str2num(s):
    idx = 0
    num = 0
    while idx < len(s):
        num *= 10
        num += int(s[idx])
        idx += 1
    return num
