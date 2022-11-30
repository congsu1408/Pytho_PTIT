def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def Emirp(n):
    if isPrime(n):
        if isPrime(int(str(n)[::-1])) and n != int(str(n)[::-1]):
            return True
    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        mark = [True]*(n+1)
        for i in range(n):
            if Emirp(i) and int(str(i)[::-1]) < n and mark[i] and mark[int(str(i)[::-1])]:
                print(i, int(str(i)[::-1]), end=" ")
                mark[i] = False
                mark[int(str(i)[::-1])] = False
        print()
