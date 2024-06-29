'''
1.T 입력
2.알파벳대문자로 구성된 문자열 S 입력
3.isPalindrome 함수를이용해서 Palindrome 이면 1 아니면 0을 반환
4.recursion 함수 호출 횟수 누적
'''

'''
n = int(input())
isP = True
idx = 0

for i in range(n):
    s = input()

    for j in range(int(len(s)/2+1)):
        idx = j+1
        if s[j] != s[len(s)-1-j]:
            isP = False
            break

    if(isP):
        print(1," ",idx)
    else:
        print(0," ",idx)
'''

def recursion(s, l, r):
    if l >= r: return 1, l+1
    elif s[l] != s[r]: return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


t = int(input())

for i in range(t):
    s = input()
    result = list(isPalindrome(s))
    print(result[0],result[1])