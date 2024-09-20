# cook your dish here
def frequencyCount(s):
    s= list(s)
    new=set(s)
    new=sorted(new)
    a=[]
    for i in new:
        a.append(i+str(s.count(i)))
    a= ''.join(a)
    return a
    

s= input()
print(frequencyCount(s))