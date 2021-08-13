from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Picker")
root.geometry("200x200")
root.iconbitmap('./favicon.ico')

def coloroutput():
    color = colorchooser.askcolor()[1]
    my_label = Label(root, text=color).pack(pady=10)
    defaultLabel = Label(root,text="    ", font=("Helvetica", 64), bg=color).pack()    

my_button = Button(root, text="Choose A Color", command=coloroutput).pack(pady=5)

root.mainloop()
