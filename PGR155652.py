# 글자별로 똑같은 과정을 반복함

def solution(s, skip, index):
    answer = ''
    # letter 별로 글자 순회 함
    for letter in s:
        # letter 별로 index 만큼 순회
        count = index
        # count 만큼 반복 (그래서 count -=1 )
        # skip 에 있는 문자는 건너뛰기 위해 for 문이 아닌 while 문으로 작성
        while count:
            # 현재 letter 'z' 일 경우 제일 처음인 'a' 로 돌아가게 만들어 줌
            if letter == 'z':
                letter = 'a'
            else:
                # 문자를 숫자로 변환 을 한다음 +1 을 하고 다시 문자로 변환
                letter = chr(ord(letter) + 1)
            # 만약 다음글자가 skip 이 없을 경우에만 count 를 -1 해준다.
            if letter not in skip:
                count -= 1
        # 나온 결과를 모두 더한다.
        answer += letter
    return answer

# ord => 아스키코드값으로 변환
# chr => 아스키코드값을 문자로 변환
# ord ('a') = 97
# chr (97) = 'a'
# chr(ord('a')+5) = f
# a -> b -> c -> d -> e -> f -> g -> h
