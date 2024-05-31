n = int(input())


for _ in range(n):
    t = input()
    score = 0
    result = 0
    for i in t:
        if i == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)
