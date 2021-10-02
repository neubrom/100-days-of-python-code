from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(3, 4)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    new_password = "".join(password_list)
    entry_password.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave fields empty!")
    else:
        is_ok = messagebox.showinfo(title=web, message=f"There are the details entered: \nEmail: {email}"
                                f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)


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


button = Button(text="Generate password", command=pass_generator)
button.grid(column=2, row=3)

button_add = Button(text="Add", width=42, command=save)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()