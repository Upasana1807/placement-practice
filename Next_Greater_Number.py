# cook your dish here
def NextGreaterNumber(n, s):
    inp= sorted(s)
    

    while True:
        s= int(s)+1
        new= sorted(str(s))
        if(inp==new):
            return s 
    
n= int(input())
s= input()
print(NextGreaterNumber(n, s))