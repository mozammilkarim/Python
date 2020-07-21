from tkinter import *
root=Tk()
root.title("Exercise 1 resizing the window")
root.geometry("644x334")

def resize():
    size=widthVal.get()+ "x" +heightVal.get()  
    print(size)
    root.geometry(size)
    
# labels
height = Label(root, text="height").grid()
width = Label(root, text="width")
width.grid(row=1)
#inputs
heightVal=StringVar()
widthVal=StringVar()

heightEntry = Entry(root, textvariable=heightVal).grid(row=0, column=1)
widthEntry = Entry(root, textvariable=widthVal ).grid(row=1, column=1)
Button(text="Submit", command=resize).grid()


root.mainloop()