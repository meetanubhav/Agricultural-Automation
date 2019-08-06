try:
  import Tkinter
except:
    import tkinter
    from tkinter import *

def showtext():
    messagebox.showinfo("Hello", "Red Button clicked")
    
def ui_main():
    top = tkinter.Tk()
    Button1= tkinter.Button(top, text ="Hello",command = showtext)
    Button1.pack()        
    top.mainloop()

if __name__ == "__main__":
    ui_main()