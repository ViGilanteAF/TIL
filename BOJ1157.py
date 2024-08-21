n = input().upper()

n_list = list(set(n)) # 중복 제거 후 n_list에 저장

lst = []

for i in n_list:            # n_list 의 각문자 i 에 대해 반복
    count = n.count(i)      # 문자열 n 에서 문자 i 가 몇번 등장하는지 세어서 count 에 저장
    lst.append(count)       # n_list 에 있는 각 문자의 등장 횟수 저장

if lst.count(max(lst)) >= 2:     # lst 에 가장큰값 이 몇번 나타나는지 세어서 2번 이상 이면 ? 출력
    print("?")

else:
    print(n_list[lst.index(max(lst))])  # 가장많이 등장한 문자가 1개뿐이라면 lst 에서 가장 큰 값의 인덱스를 찾아 해당되는 n_list의 문자를 출력
