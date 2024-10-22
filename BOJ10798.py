import sys

input = sys.stdin.readline

arr = []                                           # 2차원 배열을 저장할 리스트
result = []                                        # 최종 결과를 담을 리스트

for _ in range(5):                                 # 5번 반복
    line = input().strip()                         # 줄바꿈 과 공백을 제거 하면서 line 이라는 변수에 입력을 받음
    if 1 <= len(line) <= 15:                       # 1개 이상 15개 이하의 글자 가 입력이 될경우
        arr.append(list(line))                     # 각 문자를 리스트 형태로 변환 해서 arr 리스트 에 저장
    else:
        exit()


max_length = max(len(row) for row in arr)          # 모든 행의 길이중 최대 길이를 찾아서 max_length 변수에 저장

for col in range(max_length):                      # 최대 열 길이 만큼 반복 열(col) 인덱스 를 0 부터 max_length-1 까지 반복 해서 세로 방향 으로 문자를 읽음
    for row in arr:                                # 각 행 을 돌면서
        if col < len(row):                         # 해당 열 인덱스 가 행의 길이 보다 작은 경우 (짧은 줄에 없는 문자 는 무시)
            result.append(row[col])                # result 에 값을 저장

print("".join(result))                             # result 에 있는 모든 문자를 하나의 문자열 로 연결 해서 출력
