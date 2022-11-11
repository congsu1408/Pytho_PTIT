def Process(s):
    sum = 0
    res = 0
    for i in range(len(s)):
        while i < len(s) and s[i].isdigit():
            sum = sum*10+int(s[i])
            i += 1
            res = max(res, sum)
        sum = 0
    return res


for _ in range(int(input())):
    s = input()
    print(Process(s))
