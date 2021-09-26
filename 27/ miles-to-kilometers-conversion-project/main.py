from tkinter import *

# Window object definition
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Input box
input_box = Entry(width=10, font=("raleway", 11))
input_box.insert(END, 0)
input_box.grid(row=1, column=1)

# Label - Miles
miles = Label(text="Miles", font=("raleway", 11))
miles.grid(row=1, column=2, padx=5)

# Label = Is equal to
is_equal_to = Label(text="is equal to", font=("raleway", 11))
is_equal_to.grid(row=2, column=0)

# Label - Converted value
result = Label(text=0, font=("raleway", 11))
result.grid(row=2, column=1)

# Label - Kilometers
kilometers = Label(text="Km", font=("raleway", 11))
kilometers.grid(row=2, column=2)


# Button - To calculate
def convert():
    conversion = float(input_box.get()) * 1.609
    result.config(text=conversion, font=("raleway", 11))


calculate_button = Button(text="calculate", command=convert, font=("raleway", 11))
calculate_button.grid(row=3, column=1)


# Window on screen
window.mainloop()