'''
입력받은 것 중 이미 저장되어있는 크로아티아 알파벳 이랑 매칭되는것이 있는지 검사 후 개수 카운팅

'''
import sys

input = sys.stdin.readline

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()

for i in cro:
    w = w.replace(i, '*')


print(len(w.strip()))