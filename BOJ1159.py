n = int(input())

a = []


for _ in range(n):
    name = input()
    a.append(name[0]) #입력받은 name 들 중에 가장 첫글자들만 a배열에 저장

dup = []
for i in a:
    if a.count(i) >=5:  #a배열에 들어간 문자 의 갯수를 새서 5개 이상의 것만 dup배열에 저장
        dup.append(i)

if len(dup) > 0:
    print(''.join(sorted(set(dup)))) # set으로 중복을 제거 하고 정렬을 한뒤 문자열로 결합후 출력
else:
    print('PREDAJA')
