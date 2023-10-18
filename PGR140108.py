def solution(s):
    answer = 0
    x = s[0]
    x_count = other_count = 0
    for idx, letter in enumerate(s):
        if letter == x:
            x_count += 1
        else:
            other_count += 1
        if x_count == other_count:
            answer += 1
            if idx != len(s) - 1:
                x = s[idx+1]
            x_count = other_count = 0
    if x_count != other_count:
        answer += 1
    return answer

# ba na na
# x:  n
# x횟수: 0
# x가 아닌 글자 횟수: 0
