if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        key = 0
        for i in range(2, len(s)):
            if (s[i] != s[i-2]):
                print("NO")
                key = 1
                break
        if (key == 0):
            print("YES")
