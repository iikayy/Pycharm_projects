from tkinter import *


def button_clicked():
    miles = float(miles_entry.get())
    km = miles * 1.603944
    number.config(text=round(km))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(100, 100)
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Ariel", 12, "normal"))
is_equal_label.grid(column=1, row=2)

miles_entry = Entry(width=10)
print(miles_entry.get())
miles_entry.grid(column=3, row=1)

number = Label(text="0", font=("Ariel", 12, "normal"))
number.grid(column=3, row=2)

miles_label = Label(text="Miles", font=("Ariel", 12, "normal"))
miles_label.grid(column=4, row=1)

km_label = Label(text="Km", font=("Ariel", 12, "normal"))
km_label.grid(column=4, row=2)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=3, row=3)




window.mainloop()