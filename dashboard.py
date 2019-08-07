import tkinter as tk
from tkinter import messagebox
def showtext():
    messagebox.showinfo("Hello", "Red Button clicked")
    
def ui_main():
    window = tk.Tk()
    window.title("GUI")
    window.geometry('400x400')
    window.configure(background="grey")
    btn1 = tk.Button(window, text="B1",fg="green",command=showtext)
    btn1.grid(row=1, column=1, rowspan=2, pady=30, padx=30)
    btn1.config(height=2, width=6)
    btn2= tk.Button(window, text="B2",fg="green",command=showtext)
    btn2.config(height=2, width=6)
    btn2.grid(row=2, column=1, rowspan=2, pady=30, padx=30)
    btn3 = tk.Button(window, text="B3",fg="green",command=showtext)
    btn3.config(height=2, width=6)
    btn3.grid(row=3, column=1, rowspan=2,  pady=30, padx=30)

    a1 = tk.Entry(window)
    a1.grid(row=1, column=2, rowspan=2, pady=30, padx=60)
    b1 = tk.Entry(window)
    b1.grid(row=2, column=2, rowspan=2, pady=60, padx=60)
    c1 = tk.Entry(window)
    c1.grid(row=3, column=2, rowspan=2, pady=120, padx=60)
    window.mainloop()

if __name__ == "__main__":
    ui_main()
