n = input()
sum = 0
for i in range(len(n)):
    now = n[i]
    if (now == 'A' or now == 'B' or now == 'C'):
        sum += 3
    elif (now == 'D' or now == 'E' or now == 'F'):
        sum += 4
    elif (now == 'G' or now == 'H' or now == 'I'):
        sum += 5
    elif (now == 'J' or now == 'K' or now == 'L'):
        sum += 6
    elif (now == 'M' or now == 'N' or now == 'O'):
        sum += 7
    elif (now == 'P' or now == 'Q' or now == 'R' or now == 'S'):
        sum += 8
    elif (now == 'T' or now == 'U' or now == 'V'):
        sum += 9
    elif (now == 'W' or now == 'X' or now == 'Y' or now == 'Z'):
        sum += 10
print(sum)
