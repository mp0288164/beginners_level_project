import tkinter as tk 
import tkinter.messagebox
from tkinter.constants import SUNKEN
window=tk.Tk()
window.title('calculater')
frame=tk.Frame(master=window,bg='skyblue',padx=10)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
entry.grid(row=0,coloumn=0,coloumnspan=3,ipady=2,pady=2)

def myclick(number):
    entry.insert(tk.END,number)
def equal():
    try:
        y=srt(eval(entry.grt()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo('Error','syntax Error')
def clear():
    entry.delete(0,tk.END)

bu1=tk.Button(master=frame,text='1',padx=15,pady=5,width=3,command=lambda:myclick(1))
bu1.grid(row=1,coloumn=0,pady=2)

bu2.grid(row=1,coloumn=0,pady=2)
bu2=tk.Button(master=frame,text='2',padx=15,pady=5,width=3,command=lambda:myclick(2))

bu3.grid(row=1,coloumn=0,pady=2)
bu3=tk.Button(master=frame,text='3',padx=15,pady=5,width=3,command=lambda:myclick(3))

bu4.grid(row=1,coloumn=0,pady=2)
bu4=tk.Button(master=frame,text='4',padx=15,pady=5,width=3,command=lambda:myclick(4))

bu5.grid(row=1,coloumn=0,pady=2)
bu5=tk.Button(master=frame,text='5',padx=15,pady=5,width=3,command=lambda:myclick(5))

bu6.grid(row=1,coloumn=0,pady=2)
bu6=tk.Button(master=frame,text='6',padx=15,pady=5,width=3,command=lambda:myclick(6))

bu7.grid(row=1,coloumn=0,pady=2)
bu7=tk.Button(master=frame,text='7',padx=15,pady=5,width=3,command=lambda:myclick(7))

bu8.grid(row=1,coloumn=0,pady=2)
bu8=tk.Button(master=frame,text='8',padx=15,pady=5,width=3,command=lambda:myclick(8))

bu9.grid(row=1,coloumn=0,pady=2)
bu9=tk.Button(master=frame,text='9',padx=15,pady=5,width=3,command=lambda:myclick(9))

bu0.grid(row=1,coloumn=0,pady=2)
bu0=tk.Button(master=frame,text='0',padx=15,pady=5,width=3,command=lambda:myclick(0))

bu_add.grid(row=1,coloumn=0,pady=2)
bu_add=tk.Button(master=frame,text='+',padx=15,pady=5,width=3,command=lambda:myclick('+'))

bu_sub.grid(row=1,coloumn=0,pady=2)
bu_sub=tk.Button(master=frame,text='-',padx=15,pady=5,width=3,command=lambda:myclick('-'))

bu_mul.grid(row=1,coloumn=0,pady=2)
bu_mul=tk.Button(master=frame,text='*',padx=15,pady=5,width=3,command=lambda:myclick('*'))

bu_div.grid(row=1,coloumn=0,pady=2)
bu_div=tk.Button(master=frame,text='/',padx=15,pady=5,width=3,command=lambda:myclick('/'))

bu_clear.grid(row=6,coloumn=0,pady=2)
bu_clear=tk.Button(master=frame,text='clear',padx=15,pady=5, width=12,command=clear)

bu_equal.grid(row=6,coloum=0,pady=2)
bu_equal=tk.Button(master=frame,text='=',padx=15,pady=5, width=9,command=equal)
bu_equal.grid(row=7,coloum=0,columnspan=3,pady=2)

window.mainloop()