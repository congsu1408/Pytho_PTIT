if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        n = input()
        i = 0
        count = 0
        while i < len(s):
            tmp = s[i:len(n)+i]
            if tmp == n:
                s = s[len(n):]
                count += 1
            else:
                i += 1
        print(count)
