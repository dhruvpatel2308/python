class Stack():
    def __init__(self,n):
        self.items=[]
        self.n=n
    def push(self,b):
        if len(self.items)<self.n:
            self.items.append(b)
        else:
            print("Stack is full")
    def show(self):
        print(self.items)
    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            return "stack is empty"
    def peep(self):
        if len(self.items)>0:
            print(self.items[-1])
        else:
            print("Stack is empty")

d=Stack(5)
x=d.pop()
print(x)
d.peep()
d.push("dp")
d.push("dhruv")
d.push("d")
d.show()
x=d.pop()
print(x)
d.show()
d.peep()
d.push("a")
d.push("b")
d.push("c")
d.show()
d.push("d")
