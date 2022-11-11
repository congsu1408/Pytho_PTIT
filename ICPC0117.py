m = {"-1"}
for _ in range(int(input())):
    s = input()
    if s not in m:
        m.add(s)
print(len(m)-1)
