
s = input()

'''for i in range(26):
    temp = -1
    for j in range(len(s)):
        if (s[i] - 'a' == i):
            temp = j
            break
print(temp, " ")
'''
a = [-1] * 26   # a(97), b(98), c, d, ... z(122)

for i in range(len(s)):
    if a[ord(s[i])-97] == -1:   # 기록되어 있지 않은 경우만 기록
        a[ord(s[i])-97] = i  # 문제에서 소문자로만 이루어 져있기 때문에 -97만 함

print(' '.join(str(i) for i in a))
