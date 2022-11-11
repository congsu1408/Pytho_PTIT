from math import factorial


def isKrishnamurthy(n):
    sum = 0
    temp = n
    while temp > 0:
        sum += factorial(temp % 10)
        temp //= 10
    return sum == n


for _ in range(int(input())):
    n = int(input())
    if isKrishnamurthy(n):
        print("Yes")
    else:
        print("No")
