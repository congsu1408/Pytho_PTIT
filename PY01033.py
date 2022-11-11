import math


def GCD(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False


L, R = map(int, input().split())
for i in range(L, R+1):
    for j in range(i+1, R+1):
        if GCD(i, j) == 1:
            for k in range(j+1, R+1):
                if GCD(j, k) == 1 and GCD(i, k) == 1:
                    print("(", end="")
                    print(i, end=", ")
                    print(j, end=", ")
                    print(k, end=")\n")
