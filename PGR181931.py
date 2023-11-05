
def solution(a, d, included):
    # if 에  따라서 append 를 해야 하는지 말아야 하는지 에 대한 조건이 있을 경우
    # if 는 list comprehension 맨뒤에 붙여준다.
    # i: d * (i-1) + a
    return sum(d * idx + a for idx, included in enumerate(included) if included)
