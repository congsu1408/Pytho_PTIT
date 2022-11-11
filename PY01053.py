def Process(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    n = input()
    Process(n)
