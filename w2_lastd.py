#"python3"
n= int(input())
res=0
if n<2:
    res=n
else :
    a,b =0,1
    for i in range (1,n):
        a,b= b, (a+b)%10
        res= b
print(res)