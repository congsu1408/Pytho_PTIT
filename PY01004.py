import math


def isPrime(n):
    if n<2: return 0
    if n<=3: return 1
    for i in range(5,math.sqrt(n)+1):
        if n%i==0: return 0
    return 1

for t in range(int(input())):
    n=int(input())
    k=0
    for i in range(1,n):
        if math.gcd(n,i)==1:
            k=k+1
    print('YNEOS'[~isPrime(k)%2::2])
        
