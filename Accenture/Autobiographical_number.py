# cook your dish here
n=input()
n=list(n)
flag=0
for i in range(len(n)):
    if(n.count(str(i))==int(n[i])):
        flag+=1
if(len(n)==flag):
    arr=set(n)
    print(len(arr))