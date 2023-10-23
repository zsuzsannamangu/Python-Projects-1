import tkinter as tk
from tkinter import *
import webbrowser
import os

#The webbrowser module is a python library that allows
#you to create web documents and display them in the browser

#text content should change according to user input

#Your task is to create a new function within the ParentWindow class
#that takes user input as text and then displays that custom text
#on the generated web page.




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
    
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10, 10), pady=(10, 10))

        
    def defaultHTML(self):
        htmlText = "Stay tuned for an amazing summer sale!"
        # to open/create a new html file in the write mode:
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # writing the code into the file:
        htmlFile.write(htmlContent)
        # close the file:
        htmlFile.close()
        filename = 'file:///'+os.getcwd()+'/' + 'index.html'
        webbrowser.open_new_tab(filename)
        print("hi")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






