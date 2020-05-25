import operator
s=input()
a=dict()
for i in s:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
b=dict(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
for i in b:
    print(i*b[i],end="")
