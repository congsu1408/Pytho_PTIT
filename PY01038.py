def Process(n):
    sum = int(n)
    i = 0
    while (i <= 1000):
        if (sum % 7 == 0):
            return sum
        else:
            sum = int(n)+int(n[::-1])
            n = str(sum)
            i += 1
    if (i > 1000):
        return -1


for _ in range(int(input())):
    n = input()
    print(Process(n))
