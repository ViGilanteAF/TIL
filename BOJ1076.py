n = input()
m = input()
z = input()

colour = ['black', 'brown', 'red','orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
time = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]


for i in range(len(colour)):
    tmp1= colour.index(n)
    tmp2= colour.index(m)
    tmp3 = colour.index(z)
    for j in range(len(time)):
        tmp4 = time[tmp3]

print(((tmp1*10)+tmp2)*tmp4)