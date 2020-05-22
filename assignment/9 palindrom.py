s=input("string:")
i=0
flag=0
while i<len(s):
    if s[i]!=s[-(i+1)]:
        flag=1
        break
    i+=1

if flag!=1:
    print("palindrom")
else:
    print("not palindrom")