class P1():
    def __init__(self):
        print("Constructor called")
    def show(self):
        print("method of the class")
    def __del__(self):
        print("Destructor called")
p=P1()
p.show()
o=P1()
o.show()