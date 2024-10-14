import itertools                                        # 조합 라이브러리
i = []
for _ in range(9):
    a = int(input())
    i.append(a)

combination = list(itertools.combinations(i, 7))    # 9명중 7명을 고르는 모든 조합을 구함
while True:                                            # 무한루프
    beach = combination.pop()                          # 조합 리스트 에서 마지막 조합을 꺼냄
    if sum(beach) == 100:                              # 합이 100인 조합을 찾으면
        q = sorted(list(beach))                        # 조합을 오름차순 으로 정렬함
        for i in q:
            print(i)                                   # 정렬된 값을 출력
        break                                          # 정답을 찾으면 반복 종료