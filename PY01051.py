def check(n):
    if n != n[::-1] or len(n) == 1:
        return False
    return True


for _ in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if check(str(sum)):
        print("YES")
    else:
        print("NO")
