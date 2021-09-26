from tkinter import *

# Window object definition
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Input box
input_box = Entry(width=10, font=("Arial", 14))
input_box.insert(END, 0)
input_box.grid(row=1, column=1)

# Label - Miles
miles = Label(text="Miles", font=("Arial", 14))
miles.grid(row=1, column=2, padx=5)

# Label = Is equal to
is_equal_to = Label(text="is equal to", font=("Arial", 14))
is_equal_to.grid(row=2, column=0)

# Label - Converted value
result = Label(text=0, font=("Arial", 14))
result.grid(row=2, column=1)

# Label - Kilometers
kilometers = Label(text="Km", font=("Arial", 14))
kilometers.grid(row=2, column=2)


# Button - To calculate
def convert():
    conversion = float(input_box.get()) * 1.609
    result.config(text=conversion, font=("Arial", 14))


calculate_button = Button(text="calculate", command=convert, font=("Arial", 14))
calculate_button.grid(row=3, column=1)


# Window on screen
window.mainloop()