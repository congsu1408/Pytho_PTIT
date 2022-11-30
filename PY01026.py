if __name__ == '__main__':
    for _ in range(1, int(input())+1):
        s1 = list(input())
        s2 = list(input())
        if sorted(s1) == sorted(s2):
            print("Test {}: YES".format(_))
        else:
            print("Test {}: NO".format(_))
