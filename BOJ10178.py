n = int(input())

for i in range(n):
    c, v = map(int, input().split())

    m = c//v
    t = c % v
    print("You get " + str(m) +
          " piece(s) and your dad gets " + str(t) + " piece(s).")
