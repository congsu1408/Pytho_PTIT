for _ in range(int(input())):
    p, q = [x for x in input().split()]
    X1 = input().strip()
    if (X1.count(' ')):
        X1, X2 = X1.split()
    else:
        X2 = input()
    m = max(p, q)
    n = min(p, q)
    print(int(X1.replace(m, n)) +
          int(X2.replace(m, n)), end=" ")
    print(int(X1.replace(n, m)) +
          int(X2.replace(n, m)))
