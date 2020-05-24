def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Denominator is zero")

n1,n2=map(int,input("enter  numbers:").split())
div(n1,n2)

def f1(fname):
    try:
        f=open(fname)
        for line in f.readline():
            print(line,end="")
    except FileNotFoundError:
        print("File not found error")


n1=input("enter file name:")
f1(n1)