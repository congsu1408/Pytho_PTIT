for _ in range(int(input())):
    print("YNEOS"[any(x not in '012'for x in input())::2])
