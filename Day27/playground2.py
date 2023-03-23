import tkinter
from tkinter import Button
from tkinter import Entry

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


## Label
my_label = tkinter.Label(text="I am label",font= ("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.config(text="I got clicked")
#
my_label["text"] = "New_Text"
#my_label.config(text="Button got clicked")
#my_label.pack(expand=True)
my_label.pack()


# Entry
input = Entry(width=10)
input.pack()


## Button
def button_clicked():
    #my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text= new_text)


    #print("I Got Clicked")


button = Button(text="ClickMe",font=("Arial", 16, "bold"),command=button_clicked)
button.pack(side="bottom")






window.mainloop()