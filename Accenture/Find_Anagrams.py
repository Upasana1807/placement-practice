# cook your dish here
def FindAnagrams(arr1, arr2):
    arr1= list(arr1)
    arr2= list(arr2)
    arr1.sort()
    arr2.sort()
    if(arr1==arr2):
        return("Yes")
    else:
        return("No")
    


arr1=input()
arr2= input()
print(FindAnagrams(arr1, arr2))