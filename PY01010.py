for t in range(int(input())):
    s=input();print("YNEOS"[any(x not in s[0]for x in s[len(s)-2])or any(x not in s[1]for x in s[len(s)-1])::2])