#"python3"
n = int(input())
arr = [int(el) for el in input().split()]
arrs=[]
x=0
for i in range (n):
    x= max(x,arr[i])
ind= arr.index(x)
arr.sort()
y=len(arr)
arrs=arr[:y-1]
y=0
for i in range (n-1):
    y=max(y,arrs[i])
print(x*y)
    


