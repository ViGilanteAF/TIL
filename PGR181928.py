def solution(num_list):
    odds =''.join([str(num) for num in num_list if num %2 ])
    evens = ''.join([str(num) for num in num_list if num %2 == 0])
    
    return int(odds) + int(evens)