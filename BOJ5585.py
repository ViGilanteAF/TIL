n = int(input())
count = 0
calc = 1000 - n

while (n < 1000):
    if (calc > 500):
        calc = calc - 500
        count += 1
    elif (calc >= 100):
        calc = calc-100
        count += 1
    elif (calc >= 50):
        calc = calc-50
        count += 1
    elif (calc >= 10):
        calc = calc-10
        count += 1
    elif (calc >= 5):
        calc = calc-5
        count += 1
    elif (calc >= 1):
        calc = calc-1
        count += 1
    elif (calc == 0):
        break

print(count)
