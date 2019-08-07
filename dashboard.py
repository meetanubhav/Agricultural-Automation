import tkinter as tk
from tkinter import messagebox
import db
def showtext():
    # msg = messagebox.showinfo("Say Hello", "Hello World")
    ui_obj=ui_main()
    ui_obj.showtext1()
class ui_main:
    window = tk.Tk()
    window.title("Agro")
    frame = tk.Frame(window)
    window.geometry('800x800')
    window.configure(background="grey")
    lblinfo = tk.Label(window, font=('aria', 30, 'bold'), text="Agrosight", fg="steel blue",  bd=10, anchor='center')
    lblinfo.grid(row=0, column=2, pady=30, padx=30)
    c="red"
    def fun_btn1(window,c):
        btn1 = tk.Button(window, text="B1",fg="black",background=c,command=showtext)
        btn1.grid(row=1, column=1, rowspan=2, pady=30, padx=30)
        btn1.config(height=2, width=6)
    fun_btn1(window,c)
    def showtext1(self):
        print()
        self.fun_btn1(self.window,"black")
    btn2= tk.Button(window, text="B2",fg="green",command=showtext)
    btn2.config(height=2, width=6)
    btn2.grid(row=2, column=1, rowspan=2, pady=30, padx=30)
    btn3 = tk.Button(window, text="B3",fg="green",command=showtext)
    btn3.config(height=2, width=6)
    btn3.grid(row=3, column=1, rowspan=2,  pady=30, padx=30)
    x=1.23
    y=2.2
    z=3.2
    a1 = tk.Label(window,  text=x)
    a1.grid(row=1, column=2, rowspan=2, pady=30, padx=60)
    b1 = tk.Label(window, text=y)
    b1.grid(row=2, column=2, rowspan=2, pady=60, padx=60)
    c1 = tk.Label(window, text=z)
    c1.grid(row=3, column=2, rowspan=2, pady=120, padx=60)
    window.mainloop()

if __name__ == "__main__":
    ui_main()
