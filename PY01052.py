def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])
        if isPrime(sum):
            print("YES")
        else:
            print("NO")
