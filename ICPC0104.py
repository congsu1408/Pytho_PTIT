def Process(s):
    sum = 0
    res = 1e9
    for i in range(len(s)):
        if s[i].isdigit() == False:
            if i != 0 and s[i-1].isdigit():
                res = min(res, sum)
                sum = 0
        else:
            sum = sum*10+int(s[i])
    return res


for _ in range(int(input())):
    s = input()
    print(Process(s))
