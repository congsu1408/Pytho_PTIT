n = int(input())
a = [int(x) for x in input().split()]
res = []
for i in a:
    if len(res) == 0:
        res = res+[i]
    else:
        if (res[-1]+i) % 2 == 0:
            res.pop()
        else:
            res = res+[i]
print(len(res))
