'''
배열에 문자열 갯수대로 나눠서 저장후 문자열 갯수가 가장 적은수 부터 출력
[{a},{ab},{abc},{abcd}] 이런식으로...
'''
n = int(input())
arr = [set() for _ in range(20001)]
for _ in range(n):
    a = input()
    arr[len(a)].add(a)
for i in range(20001):
    for j in sorted(arr[i]):
        print(j)