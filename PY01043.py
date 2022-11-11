def Process(n):
    if n != n[::-1] or len(n) % 2 == 1:
        return False
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True


for _ in range(int(input())):
    n = input()
    for i in range(22, int(n), 2):
        if Process(str(i)):
            print(i, end=' ')
    print()
