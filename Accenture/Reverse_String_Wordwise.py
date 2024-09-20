# cook your dish here
def ReverseStringWordwise(s):
    s= s.split()
    s.reverse()
    s= ' '.join(s)
    return s
    

s= input()
print(ReverseStringWordwise(s))