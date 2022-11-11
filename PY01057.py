def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = input()
    key = 0
    for i in range(len(n)):
        if isPrime(i):
            if isPrime(int(n[i])) == False:
                key = 1
                break
        if isPrime(i) == False:
            if isPrime(int(n[i])):
                key = 1
                break
    if key == 1:
        print("NO")
    else:
        print("YES")
