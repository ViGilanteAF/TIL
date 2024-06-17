n, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()

print(x[len(x)-k])

# print(sorted(x)[-k])
'''
sort 로 오름차순 정렬한뒤 상을 받는 사람의 수 인 k 명을 뒤에서 부터 세서 
나타내준다.
'''
