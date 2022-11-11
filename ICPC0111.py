for _ in range(int(input())):
    N, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(d, N):
        print(a[i], end=" ")
    for i in range(0, d):
        print(a[i], end=" ")
    print()
