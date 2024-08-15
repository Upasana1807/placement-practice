# cook your dish here
def highestLengthPallindromeWord(s):
    li= s.split()
    arr=[]
    for i in li:
        if i==i[::-1]:
            arr.append(i)
        arr.sort(key=len)
    return arr[-1]

s= input()
print(highestLengthPallindromeWord(s))