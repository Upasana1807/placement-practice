def OpBinaryString(s):
    a=int(s[0])
    i=1
    while i< len(s):
        if s[i]=='A':
            a&=int(s[i+1])
        elif s[i]=='B':
            a|=int(s[i+1])
        elif s[i]=='C':
            a^=int(s[i+1])
        i+=2
    return a
s=input()
print(OpBinaryString(s))

