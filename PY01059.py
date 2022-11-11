def sum(s):
    sum = 0
    for i in range(0, len(s), 2):
        sum += int(s[i])
    return sum


def mul(s):
    multi = 1
    for i in range(1, len(s), 2):
        if s[i] != "0":
            multi *= int(s[i])
    if multi == 1:
        return 0
    else:
        return multi


for _ in range(int(input())):
    s = input()
    print(sum(s), end=" ")
    print(mul(s))
