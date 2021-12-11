from tkinter import *
import tkinter.messagebox as tmsg
import os 
from tkinter.filedialog import askopenfilename,asksaveasfilename



root = Tk()
root.geometry('1000x500')
root.title("Rahul's Notepad")
# root.wm_iconbitmap('icon.ico')

File=None
mainmenu = Menu(root)

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)
def open():
    global file
    file =askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()
def save():
    file=asksaveasfilename()
    pass
def exit():
    a=tmsg.askyesno('Exit','Do you want to exit')
    if a==YES:
        root.destroy()
    elif a==NO:
        pass

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label='New',command=new)
m1.add_command(label='Open',command=open)
m1.add_command(label='Save',command=save)
m1.add_command(label='Exit',command=exit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File',menu=m1)

def cut():
    text.event_generate('<<Cut>>')
def copy():
    text.event_generate('<<Copy>>')
def paste():
    text.event_generate('<<Paste>>')
def select_all():
    text.tag_add('sel',1.0,'end')
def clear():
    text.delete(1.0,END)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label='Cut',command=cut)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)
m2.add_command(label='Select All',command=select_all)
m2.add_command(label='Clear All',command=clear)
mainmenu.add_cascade(label='Edit',menu=m2)

def feedback():
    a=tmsg.askyesno('Feedback','Do you like this notepad?')
    if a==YES:
        tmsg.showinfo('Feedback','Thanks for using this Notepad \n Please Rate us Microsoft store')
    if a==NO:
        tmsg.showinfo('Feedback','If you are facing any issue please mail us at:rahul.yaduwanshi007@gmail.com \nWe will surely try to solve your issues and enhance your experience.\nKeep your app updated to get better experience. ')

def about():
    tmsg.showinfo('About this Notepad','This notepad was developed by Rahul Ranjan')

m4= Menu(mainmenu,tearoff=0)
m4.add_command(label='Send Feedback',command=feedback)
m4.add_command(label="About Rahul's notepad",command=about)
mainmenu.add_cascade(label='Help',menu=m4)
Sb = Scrollbar(root)
Sb.pack(fill=Y,side= RIGHT)

text = Text(root,yscrollcommand = Sb.set)
text.pack(fill= BOTH)
Sb.config(command=text.yview)

root.mainloop()