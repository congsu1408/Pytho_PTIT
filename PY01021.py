if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        res = ""
        sum = 0
        for i in s:
            if i.isdigit():
                sum += int(i)
            else:
                res += i
        res = sorted(res)
        print("".join(res) + str(sum))
