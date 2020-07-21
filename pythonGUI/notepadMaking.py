
from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.filedialog  as tFile
root = Tk()
root.geometry("655x444")
root.title("My Notepad")

def newFile():
    pass
def saveFile():
    tFile.asksaveasfile(filetypes='txt')
    pass
def saveAsFile():
    tFile.asksaveasfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
def openFile():
    global mytext
    file = tFile.askopenfile(mode ='a', filetypes =[('All Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
        
    
def helpFunc():
    tmsg.showinfo('Hint',"Use Your Brain, it is powerful!")
    pass


#making menu
mainmenu = Menu(root) # adds mainMenu as a menu of window

m1 = Menu(mainmenu, tearoff=0)  # adds m1 as a submenu
# tearoff removes th e dot dot thing
m1.add_command(label="New project", command=newFile)
m1.add_command(label="Save", command=saveFile)
m1.add_command(label="Save As", command=saveAsFile)
m1.add_command(label="Open File", command=openFile)
root.config(menu=mainmenu) #updates the root
mainmenu.add_cascade(label="File", menu=m1) #updates main menu items


mainmenu.add_command(label="Help", command=helpFunc)
root.config(menu=mainmenu)

#adding scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

#content area
global mytext
mytext=Text(root,font="comicsansms 22 bold",yscrollcommand = scrollbar.set)
mytext.pack(expand=TRUE,fill=BOTH)
scrollbar.config(command=mytext.yview)

root.mainloop()
