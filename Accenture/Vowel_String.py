# cook your dish here
def Vowel_String(n, arr):
    vowel= ['a', 'e', 'i', 'o', 'u']
    a=[]
    for i in arr:
        if i[0] in vowel and i[-1] in vowel:
            a.append(i)
    return ''.join(a)

n= int(input())
arr= list(input().split())
print(Vowel_String(n, arr))


