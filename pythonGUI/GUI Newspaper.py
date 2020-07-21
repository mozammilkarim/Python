from requests import get
from tkinter import *
root = Tk() #works as a base thing
root.geometry("744x133")    #size
root.title("My GUI Newspaper")

# api-endpoint 
# news Api-  2ef0f7cac94542dbb96469302e92182d
URL = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-17&sortBy=publishedAt&apiKey=2ef0f7cac94542dbb96469302e92182d"
  

# sending get request and saving the response as response object 
r = get(url = URL) 
  
# extracting data in json format 
data = r.json()

global contentNews
contentNews=''
for item in range(0,len(data['articles'])):
    # global contentNews
    contentNews+='\n'
    contentNews+=data['articles'][item]['title']

title_label = Label(text=contentNews)
title_label.pack()

root.mainloop()
