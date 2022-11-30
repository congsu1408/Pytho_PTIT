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


def sumDigit(n):
    return sum(int(x) for x in str(n))


def isPrimeSum(n):
    return isPrime(sumDigit(n))


def isPrimeDigit(n):
    return any(isPrime(int(x)) for x in str(n))


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        if isPrime(n) and isPrimeSum(n) and isPrimeDigit(n) and isPrime(int(str(n)[::-1])):
            print("Yes")
        else:
            print("No")
