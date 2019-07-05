#"python3"
n= int(input())
f = [0,1]
i=2
if n>1:
    while i<= n:
        f.append(f[i-1]+ f[i-2])
        i+=1
print(f[n])
