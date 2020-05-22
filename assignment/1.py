a=eval(input("first:"))
b=eval(input("second:"))
x=(input("operator:"))

if x=="*":
    print(a*b)
elif x=="/":
    if b!=0:
        print(a/b)
    else:
        print("error")
elif x=="%":
    if b!=0:
        print(a%b)
    else:
        print("error")
elif x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
else:
    print("enter valid operator")