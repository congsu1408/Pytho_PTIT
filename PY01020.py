for t in range(int(input())):
    s=input();print('YNEOS'[any(x not in'8'for x in s[len(s)-2])or any(x not in '6' for x in s[len(s)-1])::2])