a, b, v, = map(int, input().split())

c = a - b
day = (v-b)/c

if((v-b)%c != 0):
    day +=1

print(int(day))