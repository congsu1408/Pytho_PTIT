for t in range(int(input())):
    s=input()
    print('YNEOS'[any(x not in'47'for x in s)::2])