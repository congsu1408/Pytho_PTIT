P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    if s == "0":
        break
    k, s = s.split()
    k = int(k)
    res = ''
    for i in s:
        j = P.find(i)
        res += P[(j+k) % 28]
    print(res[::-1])
