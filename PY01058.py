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


if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        prime = isPrime()
        print("YES" if prime[int(n[-4::])] else "NO")
