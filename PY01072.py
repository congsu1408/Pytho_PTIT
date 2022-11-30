from itertools import combinations


if __name__ == '__main__':
    a, k = map(int, input().split())
    u = [int(i) for i in input().split()]
    u = sorted(list(set(u)))
    comb = combinations(u, k)
    for i in comb:
        print(*i, sep=" ")
