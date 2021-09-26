from tkinter import *

window = Tk()
window.title("First GUI programm")
window.minsize(width=500, height=300)

#Label

my_lable = Label(text="New Label", font=("Arial", 24))
my_lable.pack()

#Button


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text=new_text)


button = Button(text="Click", command=button_clicked)
button.pack()

#Entry

input = Entry()
input.pack()

window.mainloop()

