def CounttheOccurrences (arr, n):    
     return arr.count(n)
 
arr= list(map(int, input().split()))
n= int(input())
print(CounttheOccurrences (arr, n))