a= list(map(int, input().split()))
diff= min((a[1]-a[0]), (a[2]-a[1]))
for i in range(len(a)-1):
    if((a[i+1]-a[i])!= diff):
        print(a[i]+diff)
        break