from tkinter import *
r=Tk()
r.title("Calculator")

e=Entry(r,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def btnclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current+str(number))


    
def btnadd():    
    a=e.get()
    global f1
    global math
    math="addition"
    f1=int(a)
    e.delete(0,END)
    
    
def btnequal():
    b=e.get()
    global f2
    f2=int(b)
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f1+f2)
    elif math=="sub":
        e.insert(0,f1-f2)
    elif math=="mul":
        e.insert(0,f1*f2)
    elif math=="division":
        e.insert(0,f1/f2)
    
def btnclear():
    e.delete(0,END)
    
    
def btnsub():
    a=e.get()
    global f1
    global math
    math="sub"
    f1=int(a)
    e.delete(0,END)
    

def btndiv():
    a=e.get()
    global f1
    global math
    math="division"
    f1=int(a)
    e.delete(0,END)
     



def btnmul():
    a=e.get()
    global f1
    global math
    math="mul"
    f1=int(a)
    e.delete(0,END)
    
    return
b1=Button(r,text="1",padx=40,pady=20,command=lambda:btnclick(1))
b2=Button(r,text="2",padx=40,pady=20,command=lambda:btnclick(2))
b3=Button(r,text="3",padx=40,pady=20,command=lambda:btnclick(3))
b4=Button(r,text="4",padx=40,pady=20,command=lambda:btnclick(4))
b5=Button(r,text="5",padx=40,pady=20,command=lambda:btnclick(5))
b6=Button(r,text="6",padx=40,pady=20,command=lambda:btnclick(6))
b7=Button(r,text="7",padx=40,pady=20,command=lambda:btnclick(7))
b8=Button(r,text="8",padx=40,pady=20,command=lambda:btnclick(8))
b9=Button(r,text="9",padx=40,pady=20,command=lambda:btnclick(9))
b0=Button(r,text="0",padx=88,pady=20,command=lambda:btnclick(0))
bequal=Button(r,text="=",padx=40,pady=20,command=btnequal)
badd=Button(r,text="+",padx=40,pady=20,command=lambda:btnadd())
bsub=Button(r,text="-",padx=40,pady=20,command=lambda:btnsub())
bclear=Button(r,text="C",padx=40,pady=20,command=btnclear)
bmul=Button(r,text="*",padx=40,pady=20,command=lambda:btnmul())
bdiv=Button(r,text="/",padx=40,pady=20,command=lambda:btndiv())


#put button on screen
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0,columnspan=2)

bequal.grid(row=5,column=2)
badd.grid(row=5,column=0)
bsub.grid(row=5,column=1)
bmul.grid(row=6,column=0)
bdiv.grid(row=6,column=1)
bclear.grid(row=4,column=2)
r.mainloop()