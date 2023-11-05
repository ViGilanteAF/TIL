# def solution(my_string, index_list):
#     answer = (my_string[idx] for idx in index_list)
#     return ''.join(answer)


def solution(my_string, index_list):
    return ''.join(my_string[idx] for idx in index_list)
