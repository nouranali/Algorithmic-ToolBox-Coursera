#"python3
a = int(input())
b = int(input())
def gcd(a,b):
    if b==0:
        return a
    k=a%b
    return gcd(b,k)
print(gcd(a,b))



