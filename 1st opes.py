from tkinter import *
win=Tk() #windows create
win.geometry("500x400") # windows size user input type
win.resizable(0,0) #windows size is fixed
def show():# 
    l1=Label(win,text="button clicked")# show the code button clicked in terminal
    l1.pack() # show the code in windows " the show code is button clicked"
b1=Button(win,text="click button",height=3,width=10,command=show) # button fucation use to create and text fucation use to show the "click button" and command fucation use to bind to text fucation.
b1.pack() #show the text
win.title("code code simple") #windows title create
win.mainloop() #windows create and show the moniter