
from tkinter import *
import pandas
import random
import csv


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash cards EN - FR")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def new_word():
    current_card = random.choice(to_learn)
    canvas.config(card_title, text="French")
    canvas.config(card_word, text=current_card["French"])

canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 156, text="Text", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 256, text="word", font=("Ariel", 50, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

photo_right = PhotoImage(file=r"images/right.png")
button_right = Button(image=photo_right, command=new_word)
button_right.config(bg=BACKGROUND_COLOR)
button_right.grid(column=1, row=1)


photo_wrong = PhotoImage(file=r"images/wrong.png")
button_wrong = Button(image=photo_wrong, command=new_word)
button_wrong.config(bg=BACKGROUND_COLOR)
button_wrong.grid(column=0, row=1)

window.mainloop()

