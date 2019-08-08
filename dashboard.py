import tkinter as tk
from tkinter import messagebox
import random
# import db
def welcome_screen():
	global welscr
	welscr = tk.Tk()
	# msg = messagebox.showinfo("Farmer's Friend","Welcome")
	frame = tk.Frame(welscr)
	welscr.geometry('800x800')
	welscr.configure(background="green")
	btn1 = tk.Button(welscr, text="B1",fg="white",background="black",command=showtext)
	btn1.grid(row=1, column=1, rowspan=2, pady=30, padx=30)
	btn1.config(height=2, width=6)
	welscr.mainloop()
	# print("hello")
def showtext():
    # ui_obj=ui_main()
    # ui_obj.showtext1()
    # if(yy==2):
    try:
    	window.destroy()
    except:
    	welscr.destroy()
    	# ui_main
    print("executed")
class ui_main:
    global window;window = tk.Tk()
    window.title("Agro")
    frame = tk.Frame(window)
    window.geometry('800x800')
    window.configure(background="green")
    lblinfo = tk.Label(window, font=('aria', 30, 'bold'), text="Agrosight", fg="steel blue",  bd=10, anchor='center')
    lblinfo.grid(row=0, column=2, pady=30, padx=30)
    c="red"
    def fun_btn1(window,c):
        btn1 = tk.Button(window, text="B1",fg="white",background=c,command=showtext)
        btn1.grid(row=1, column=1, rowspan=2, pady=30, padx=30)
        btn1.config(height=2, width=6)
    def fun_btn2(window,c):
      btn2= tk.Button(window, text="B2",fg="white",background=c,command=showtext)
      btn2.config(height=2, width=6)
      btn2.grid(row=2, column=1, rowspan=2, pady=30, padx=30)
    def fun_btn3(window,c):
      btn3 = tk.Button(window, text="B3",fg="white",background=c,command=showtext)
      btn3.config(height=2, width=6)
      btn3.grid(row=3, column=1, rowspan=2,  pady=30, padx=30)
    x=random.randrange(20,50,3)
    y=random.randrange(20,50,3)
    z=random.randrange(20,50,3)
    def label1(window,x):
      a1 = tk.Label(window,  text=x)
      a1.grid(row=1, column=2, rowspan=2, pady=30, padx=60)
    def label2(window,y):
      b1 = tk.Label(window, text=y)
      b1.grid(row=2, column=2, rowspan=2, pady=60, padx=60)
    def label3(window,z):
      c1 = tk.Label(window, text=z)
      c1.grid(row=3, column=2, rowspan=2, pady=120, padx=60)
    
    # calling all the attributes
    fun_btn1(window,c)
    fun_btn2(window,c)
    fun_btn3(window,c)
    label1(window,x)
    label2(window,y)
    label3(window,z)
    window.mainloop()

if __name__ == "__main__":
    welcome_screen()
