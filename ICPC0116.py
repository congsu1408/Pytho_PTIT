for _ in range(int(input())):
    s = input()
    print('YNEOS'[s[0] != s[-1]::2])
