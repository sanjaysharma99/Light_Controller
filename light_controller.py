from tkinter import *
import serial
import time


app=Tk()

logo=PhotoImage(file='D:\Python Projects\logo.jpg')
app.iconphoto(False,logo)

app.title('Light Controller')
app.config(bg='black')
app.minsize(325,300)
app.maxsize(325,300)


var1=True
var2=True
var3=True
var4=True

def setup():
    try:
        global obj
        port=e1.get()
        port=port.upper()
        obj=serial.Serial(port)

        obj.baudrate=9600
        obj.bytesize=8
        obj.parity='N'
        obj.stopbits=1

        lb3.config(text='Connected',fg='lightgreen')
        lb3.update()

    except:
        lb3.config(text='Not Connected',fg='red')
        lb3.update()

def device1():
    global var1
    global obj
    if var1==True:
        obj.write(b'A')
        btn1.config(bg='lightgreen',activebackground='lightblue')
        var1=False
    else:
        obj.write(b'a')
        btn1.config(bg='white',activebackground='white')
        var1=True  

def device2():
    global var2
    global obj
    if var2==True:
        obj.write(b'B')
        btn2.config(bg='lightgreen',activebackground='lightblue')
        var2=False
    else:
        obj.write(b'b')
        btn2.config(bg='white',activebackground='white')
        var2=True  

def device3():
    global var3
    global obj
    if var3==True:
        obj.write(b'C')
        btn3.config(bg='lightgreen',activebackground='lightblue')
        var3=False
    else:
        obj.write(b'c')
        btn3.config(bg='white',activebackground='white')
        var3=True  

def device4():
    global var4
    global obj
    if var4==True:
        obj.write(b'D')
        btn4.config(bg='lightgreen',activebackground='lightblue')
        var4=False
    else:
        obj.write(b'd')
        btn4.config(bg='white',activebackground='white')
        var4=True  

btn1=Button(app,text='Device1',command=device1,font='italic 16 bold',bg='white',activebackground='white')
btn2=Button(app,text='Device2',command=device2,font='italic 16 bold',bg='white',activebackground='white')
btn3=Button(app,text='Device3',command=device3,font='italic 16 bold',bg='white',activebackground='white')
btn4=Button(app,text='Device4',command=device4,font='italic 16 bold',bg='white',activebackground='white')
lb1=Label(app,text='Enter Port',fg='white',font='italic 12 bold',bg='black')
e1=Entry(app,width=10,font='italic 12 bold')
btn5=Button(app,text='Connect',command=setup,font='italic 14 bold',bg='blue',activebackground='blue',fg='lightgreen',activeforeground='lightgreen')
lb2=Label(app,text='www.secretofelectronics.com',fg='white',font='italic 8 bold',bg='black')
lb3=Label(app,text=' ',fg='white',font='italic 8 bold',bg='black')

btn1.grid(row=1,column=1,padx=20,pady=20)
btn2.grid(row=1,column=2,padx=20,pady=20)
btn3.grid(row=2,column=1,padx=20,pady=20)
btn4.grid(row=2,column=2,padx=20,pady=20)
lb1.grid(row=3,column=1,padx=20,pady=10)
e1.grid(row=3,column=2,padx=20,pady=10)
btn5.grid(row=4,column=1,padx=20,pady=10)
lb3.grid(row=4,column=2,pady=5)
lb2.grid(row=5,column=2)


app.mainloop()
