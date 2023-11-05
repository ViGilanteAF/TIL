'''
문자열 겹쳐쓰기
'''
def solution(my_string, overwrite_string, s):
    # 문자열 슬라이싱 을 생각하면 쉽게 풀 수 있다.
    # 굳이 배열에 넣고 배열 돌리면서 배열에서 빼고 다시 붙이고 이렇게 쓰지 말자
    # Python 은 최근에 만들어진 언어다 설계 부터 최신방식으로 간단하게 하자
    answer = my_string[:s] + overwrite_string + \
        my_string[s+len(overwrite_string):]

    return answer
