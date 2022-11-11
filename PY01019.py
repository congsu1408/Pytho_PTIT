def Process(a, b):
    for i in range(1, len(a)):
        if abs(ord(a[i])-ord(a[i-1])) != abs(ord(b[i])-ord(b[i-1])):
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    a = input()
    b = a[::-1]
    print(Process(a, b))
