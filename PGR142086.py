def solution(s):
    answer = []
    letter2idx = {}
    for idx, letter in enumerate(s):
        if letter in letter2idx:
            answer.append(idx - letter2idx[letter])
        else:
            answer.append(-1)
        letter2idx[letter] = idx
    return answer


'''
원래 해결한 코드s
import string

def solution(s):
    answer = []
    
    for i in range(len(s)):
        temp = -1
        v = s[i]
        for j in range(i):
            v2 = s[j]
            if v2 == v:
                temp = i-j
                
        answer.append(temp)
        
    return answer

'''
