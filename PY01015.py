for t in range(int(input())):
    s=input()
    key=1
    for i in range(len(s)-1):
        if(s[i]>s[i+1]):
            print("NO")
            key=0
            break
    if(key):
        print("YES")
    