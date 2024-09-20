def MaxAreaOfTriangle (n1, n2, m1, m2):    
    return max((n1*n2*0.5), (m1*m2*0.5))

n1= int(input())
n2= int(input())
m1= int(input())
m2= int(input())
print(MaxAreaOfTriangle(n1, n2, m1, m2))