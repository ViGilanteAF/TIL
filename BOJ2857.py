notFound = True
for i in range(5):
    name = input()
    if "FBI" in name:
        notFound = False
        print(i+1, end=' ')

if notFound:
    print("HE GOT AWAY!")
