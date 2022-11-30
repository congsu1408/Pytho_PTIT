def Process(s):
    if s[0] != "6":
        return False
    if s.find("888") != -1:
        return False
    if any(x not in "68" for x in s):
        return False
    return True


if __name__ == '__main__':
    print("YES" if Process(input()) else "NO")
