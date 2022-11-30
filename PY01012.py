if __name__ == '__main__':
    s = list(input())
    s2 = input()
    c = int(input())-1
    s.insert(c, s2)
    print(''.join(s))
