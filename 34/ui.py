from tkinter import *
import pandas
import random

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "#B1DDC6"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.canvas = Canvas(width=800, height=526)

        self.card_background = self.canvas.create_image(400, 263, image=card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.cross_image = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(image=self.cross_image, highlightthickness=0, command=next_card)
        self.unknown_button.grid(row=1, column=0)

        self.check_image = PhotoImage(file="images/right.png")
        self.known_button = Button(image=self.check_image, highlightthickness=0, command=is_known)
        self.known_button.grid(row=1, column=1)

        self.window.mainloop()



