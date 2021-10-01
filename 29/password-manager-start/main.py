from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=1, row=0)

title_website = Label(text="Website", fg="black", bg="white")
title_website.grid(column=0, row=1)
entry_website = Entry(width=45)
entry_website.grid(column=1, row=1, columnspan=2)

title_email = Label(text="Email/Username:", fg="black", bg="white")
title_email.grid(column=0, row=2)
entry_email = Entry(width=45)
entry_email.grid(column=1, row=2, columnspan=2)

title_password = Label(text="Password:", fg="black", bg="white")
title_password.grid(column=0, row=3)
entry_password = Entry(width=25)
entry_password.grid(column=1, row=3)

button = Button(text="Generate password") #, command=action)
button.grid(column=2, row=3)

button_add = Button(text="Add", width=42) #, command=action)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()