def ucln(a, b):
    if a == 0:
        return b
    return ucln(b % a, a)


for _ in range(int(input())):
    a = input()
    b = a[::-1]
    a = int(a)
    b = int(b)
    if ucln(a, b) == 1:
        print('YES')
    else:
        print('NO')
