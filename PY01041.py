if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        key = 0
        if (len(s) < 3):
            print("NO")
            break
        i = 1
        while (i < len(s)):
            if (s[i] > s[i-1]):
                i += 1
            else:
                break
        if (i == len(s)):
            print("NO")
            key = 1
        else:
            while (i < len(s)-1):
                if (s[i] > s[i+1]):
                    i += 1
                else:
                    print("NO")
                    key = 1
                    break
        if (key == 0):
            print("YES")
