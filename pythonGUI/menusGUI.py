
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("733x566")
root.title("Maaz")


def myfunc():
    print("Mai ek bahut hi natkhat aur shaitaan function hoon")
    # tmsg.showinfo('hello','Learn New things')
    tmsg.showwarning('Pitega',"Duur rah mujhse")

# #Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root) # adds mainMenu as a menu of window

m1 = Menu(mainmenu, tearoff=0)  # adds m1 as a submenu
# tearoff removes th e dot dot thing
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu) #updates the root
mainmenu.add_cascade(label="File", menu=m1) #updates main menu items

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()

