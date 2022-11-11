s = input()
for _ in range(len(s)-3, 0, -3):
    s = s[:_]+','+s[_:]
print(s)
