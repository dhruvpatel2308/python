def p(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True
    else:
        return False
l=[]
a,b=map(int,input("num:").split())
for i in range(a,b+1):
    if p(i)==True:
        l.append(i)
print(l)