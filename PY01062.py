def isPrime():
    prime = [1 for i in range(1000000)]
    prime[0] = 0
    prime[1] = 0
    p = 2
    while p*p <= 1000000:
        if prime[p] == 1:
            for i in range(p*p, 1000000, p):
                prime[i] = 0
        p += 1
    return prime


def countPrimeDigits(n):
    count = 0
    for i in n:
        if int(i) == 2 or int(i) == 3 or int(i) == 5 or int(i) == 7:
            count += 1
    return count*2 > len(n)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        prime = isPrime()
        print("YES" if prime[len(n)] and countPrimeDigits(n) else "NO")
