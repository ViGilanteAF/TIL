a = int(input())
b = int(input())
c = int(input())

T = a*b*c
result = list(str(T))

for i in range(10):
    print(result.count((str(i))))
'''
a,b,c 를 입력을 받고 문자열(str)로 변환후 list[] 배열로 바꾼다
result = [1,7,0,3,7,3,0,0] 
result에 들어있는 문자열(str) 은 list로 변환후 0부터 각각의 index로 저장이 된다.
그리고 count(item) 을 이용해서 매칭되는 갯수를 리턴한 값을 for 문을 통해 i 가 0 ~ 9 까지 result 에 있는 list[] 안에 그수가 있는지 확인후 그 수 만큼 print 하면 끝

간단한 문제이나 int 끼리 곱한 값을 str 로 바꾼 뒤 list 함수를 이용해서 리스트화 시키고 count 함수를 사용하기 위해 int가 아닌
str로 바꾼 뒤 출력 해야 한다.

'''
