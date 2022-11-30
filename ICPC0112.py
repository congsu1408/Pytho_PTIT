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


def Prime_Triplet(n):
    if isPrime(n) and isPrime(n + 2) and isPrime(n + 6):
        return True
    elif isPrime(n) and isPrime(n + 4) and isPrime(n + 6):
        return True
    else:
        return False


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        count = 0
        for i in range(2, n-5):
            if Prime_Triplet(i):
                count += 1
        print(count)
