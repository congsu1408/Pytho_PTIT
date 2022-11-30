from itertools import permutations


if __name__ == '__main__':
    s = input()
    perm = permutations(s)
    for i in perm:
        print(*i, sep="")
