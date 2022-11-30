if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        sum = 0
        mul = 1
        key = 0
        for i in range(len(n)):
            if i % 2 != 0:
                sum += int(n[i])
            else:
                if int(n[i]) != 0:
                    mul *= int(n[i])
                    key = 1
        if key == 0:
            print(0, sum)
        else:
            print(mul, sum)
