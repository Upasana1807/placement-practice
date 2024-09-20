# cook your dish here
def SubString(s,n):
    if n>0:
        if n>len(s):
            return 'Invalid'
        else:
            li= s.split()
            li= li[:n]
            li= ' '.join(li)
            return li

        
s= input()
n= int(input())
print(SubString(s,n))