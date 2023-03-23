import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="I am label",font= ("Arial", 16, "bold"))
my_label.config(text="NewText")
my_label.grid(column=4,row=4)

## Button
def button_clicked():
    #new_text = input.get()
    my_label.config(text="I got clicked")
    #my_label.config(text= new_text)

button = Button(text="ClickMe",font=("Arial", 16, "bold"),command=button_clicked)
button.grid(column=1,row=1)

button1 = Button(text="Second_BTN",font=("Arial", 16, "bold"))
button1.grid(column=2,row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


window.mainloop()
































