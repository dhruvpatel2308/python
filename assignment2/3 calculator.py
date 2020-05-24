class Calc():
    def __init__(self,a):
        self.a=a
    def __add__(self, o):
        return self.a + o.a
    def __sub__(self, o):
        return self.a - o.a
    def __mul__(self, o):
        return self.a * o.a
    def __truediv__(self, o):
        if o.a==0:
            print("divide by zero")
        else:
            return self.a / o.a
    def __mod__(self, o):
        if o.a==0:
            print("modulo by zero")
        else:
            return self.a % o.a

a1=Calc(10)
b1=Calc(5)
print(a1 + b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)
print(a1%b1)
c1=Calc(0)
print(a1/c1)
print(a1%c1)