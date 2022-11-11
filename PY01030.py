def ucln(a, b):
    if a == 0:
        return b
    return ucln(b % a, a)


N, K = map(int, input().split())
count = 0
for i in range(10**(K-1), 10**K):
    if ucln(i, N) == 1:
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()
