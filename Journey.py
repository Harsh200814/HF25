# Your code here
n,a,b,c = map(int,input().split())
d = n%(a+b+c)
if n<=a:
    print(1)
elif n<=a+b:
    print(2)
elif n<=a+b+c:
    print(3)
else:
    if d==0:
        print(n//(a+b+c)*3)
    elif d<=a:
        print(n//(a+b+c)*3+1)
    elif d<=a+b:
        print(n//(a+b+c)*3+2)
    else:
        print(n//(a+b+c)*3+3)
