from tkinter import*

wn = Tk()
wn.geometry('500x500')
wn.title("calculator")
txt_input=StringVar()
operator =""

def btnclk(n):
 global operator
 operator = operator+str(n)
 txt_input.set(operator)

def btnclr():
 global operator
 operator = ""
 txt_input.set("")

def equal():
 global operator
 result=str(eval(operator))
 txt_input.set(result)
 operator=""

e1 = Entry(wn,fg='blue',bg='powderblue',bd=30,justify='right',textvariable=txt_input)
e1.grid(columnspan=4)

b1 = Button(wn, text="1",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(1))
b1.grid(row=1,column=0)

b2 = Button(wn, text="2",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(2))
b2.grid(row=1,column=1)

b3 = Button(wn, text="3",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(3))
b3.grid(row=1, column=2)

b4 = Button(wn, text="+",fg='blue',padx=16,bd=8,bg='orange',command=lambda : btnclk("+"))
b4.grid(row=1, column=3)

b5 = Button(wn, text="4",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(4))
b5.grid(row=2, column=0)

b6 = Button(wn, text="5",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(5))
b6.grid(row=2, column=1)

b7 = Button(wn, text="6",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(6))
b7.grid(row=2, column=2)

b8 = Button(wn, text="-",fg='blue',padx=16,bd=8,bg='orange',command=lambda : btnclk("-"))
b8.grid(row=2, column=3)

b9 = Button(wn, text="7",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(7))
b9.grid(row=3, column=0)

b10 = Button(wn, text="8",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(8))
b10.grid(row=3, column=1)

b11 = Button(wn, text="9",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(9))
b11.grid(row=3, column=2)

b12 = Button(wn, text="*",fg='blue',padx=16,bd=8,bg='orange',command=lambda : btnclk("*"))
b12.grid(row=3, column=3)

b13 = Button(wn, text="clr",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclr())
b13.grid(row=4, column=0)

b14 = Button(wn, text="0",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : btnclk(0))
b14.grid(row=4, column=1)

b15 = Button(wn, text="=",fg='blue',padx=16,bd=8,bg='powderblue',command=lambda : equal())
b15.grid(row=4, column=2)

b9 = Button(wn, text="/",fg='blue',padx=16,bd=8,bg='orange')
b9.grid(row=4, column=3)

wn.mainloop()
