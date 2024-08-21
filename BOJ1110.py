result = n = int(input())
count = 0

while True:
    first = n//10   # 몫만 가지가고
    second = n%10   # 나머지만 가지고
    sum = first + second   # 목+나머지
    count += 1      # 카운트 1증가
    tmp = (second*10) + sum%10  # 10의 자리 수랑 1의 자리수랑 합체
    n = tmp     # 만약 입력값과 자릿수를 합한수가 같을 경우
    if tmp == result:
        break
print(count)