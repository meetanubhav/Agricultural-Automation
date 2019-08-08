import tkinter as tk
from tkinter import *
from tkinter import messagebox
# import db
def showtext():
    # msg = messagebox.showinfo("Say Hello", "Hello World")
    # ui_obj=ui_main()
    # ui_obj.showtext1()
    try:
      window.destroy()
    except:
      scr.destroy()
      class2=ui_main()
      class2.create_ui()

class ui_main:
  def __init__(self):
    print("do nothing")
    # create_ui()
  def create_ui(self):
    global window
    window = tk.Tk()
    window.title("Agro")
    frame = tk.Frame(window)
    window.geometry('1204x1204')
    window.configure(background="#45B39D")
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
    x=1.23
    y=2.2
    z=3.2
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

class welcome_scr:
  def __init__(self):
    print("inside screen 1")
  global scr
  scr = tk.Tk()
  scr.title("Welcome to AgroFarms")
  scr.geometry('800x800')
  C = Canvas(scr, bg="blue", height=250, width=300)
  filename = PhotoImage(file = "images/homebg.png")
  background_label = Label(scr, image=filename)
  background_label.place(x=0, y=0, relwidth=1, relheight=1)
  frame = Frame(scr)
  frame.pack()
  button1 = tk.Button(scr, text="Next ➔",fg="white",background="#2874A6",command=showtext)
  # btn1.grid(row=15, column=15, rowspan=2,pady=30,padx=30)
  # btn1.config(height=2, width=10)
  button1.pack(side=BOTTOM)
  scr.mainloop()
    

if __name__ == "__main__":
    # ui_main()
    class1=welcome_scr()