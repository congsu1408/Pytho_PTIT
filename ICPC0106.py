def val(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65 + 10


def toDeci(strr):
    lenn = len(strr)
    power = 1
    num = 0
    for i in range(lenn - 1, -1, -1):
        num += val(strr[i]) * power
        power = power * 2
    return num


def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)


def fromDeci(base, inputNum):
    res = ""
    while (inputNum > 0):
        res += reVal(inputNum % base)
        inputNum //= base
    res = res[::-1]
    return res


def convertBase(s, b):
    num = toDeci(s)
    ans = fromDeci(b, num)
    print(ans)


for _ in range(int(input())):
    s = input()
    b = int(input())
    convertBase(s, b)
