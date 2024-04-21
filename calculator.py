from tkinter import * 
import tkinter.messagebox

color='gray'
c='white'
root=Tk()
root.title("CALCULATER")
root.geometry('200x200')
root.resizable(width=False,height= False)
root.configure(bg=color)

#------def
num1=IntVar()
cash=IntVar()
res=StringVar()
res_cash=StringVar()
result=IntVar()
flag=StringVar()

def print_num(a): num1.set(a)
        
def plus():
    a=in_num1.get()
    cash.set(int(a))
    res_cash.set(str(a)+"+")
    res.set(res_cash.get())
    flag.set("1")

def divide():
    flag.set("4")
    a=in_num1.get()
    cash.set(int(a))
    res_cash.set(str(a)+"/")
    res.set(res_cash.get())

def ensert():
    if flag.get()=="1":
        a=in_num1.get()
        sum=int(a)+cash.get()
        res.set(res_cash.get()+str(a)+"=")
        num1.set(sum)
        
    elif flag.get()=="4":
        a=in_num1.get()
        if a=='0':
            error_ms("divide zero")
        div=cash.get()/int(a)
        res.set(res_cash.get()+"/"+str(a)+"=")
        num1.set(div)
        
def error_ms(ms):
    if ms:
        tkinter.messagebox.showerror('Error',ms)
        
           
#-------frame
top=Frame(root,width=250,height=100,bg=color )
top.pack(side=TOP)
bottom=Frame(root,width=250,height=150)
bottom.pack(side=BOTTOM)
right=Frame(bottom,width=50,height=150,bg=color)
right.pack(side=RIGHT)
left=Frame(bottom,width=200,height=150,bg=color)
left.pack(side=LEFT)
l1=Frame(left,width=200,height=50)
l1.pack(side=BOTTOM)
l2=Frame(left,width=200,height=50)
l2.pack(side=BOTTOM)
l3=Frame(left,width=200,height=50)
l3.pack(side=BOTTOM)

#------ top
lb_res=Label(top,textvariable=res,text=888,bg=color)
lb_res.pack(side=TOP,pady=5)

in_num1=Entry(top,textvariable=num1)
in_num1.pack(side=TOP,pady=10)

#------ numbeer
zero=Button(left,text="0",width=3,height=1,bg=c,command=lambda:print_num(0))
zero.pack(side=BOTTOM, padx=5,pady=5)
one=Button(l1,text="1",width=3,height=1,bg=c,command=lambda:print_num(1))
one.pack(side=LEFT, padx=5,pady=5)
two=Button(l1,text="2",width=3,height=1,bg=c,command=lambda:print_num(2))
two.pack(side=LEFT, padx=5,pady=5)
three=Button(l1,text="3",width=3,height=1,bg=c,command=lambda:print_num(3))
three.pack(side=LEFT, padx=5,pady=5)
four=Button(l2,text="4",width=3,height=1,bg=c,command=lambda:print_num(4))
four.pack(side=LEFT, padx=5,pady=5)
five=Button(l2,text="5",width=3,height=1,bg=c,command=lambda:print_num(5))
five.pack(side=LEFT, padx=5,pady=5)
six=Button(l2,text="6",width=3,height=1,bg=c,command=lambda:print_num(6))
six.pack(side=LEFT, padx=5,pady=5)
seven=Button(l3,text="7",width=3,height=1,bg=c,command=lambda:print_num(7))
seven.pack(side=LEFT, padx=5,pady=5)
eight=Button(l3,text="8",width=3,height=1,bg=c,command=lambda:print_num(8))
eight.pack(side=LEFT, padx=5,pady=5)
nine=Button(l3,text="9",width=3,height=1,bg=c,command=lambda:print_num(9))
nine.pack(side=LEFT, padx=5,pady=5)

#------ operation
btn_plus=Button(right,text="+",width=3,height=1,bg=c,command=lambda:plus())
btn_plus.pack(side=BOTTOM, padx=1,pady=1)
btn_minus=Button(right,text="-",width=3,height=1,bg=c,command=lambda:plus())
btn_minus.pack(side=BOTTOM, padx=1,pady=1)
btn_multiply=Button(right,text="*",width=3,height=1,bg=c,command=lambda:plus())
btn_multiply.pack(side=BOTTOM, padx=1,pady=1)
btn_divide=Button(right,text="/",width=3,height=1,bg=c,command=lambda:divide())
btn_divide.pack(side=BOTTOM, padx=1,pady=1)
btn_ensert=Button(right,text="=",width=3,height=1,bg=c,command=lambda:ensert())
btn_ensert.pack(side=BOTTOM, padx=1,pady=1)

root.mainloop()





#if int(number1.get())==0:
     #num1.set(a)
#elif int(number2.get())==0:
    # num2.set(a)
#number2=Entry(top,textvariable=num2)
#number2.pack(side=TOP,pady=10)