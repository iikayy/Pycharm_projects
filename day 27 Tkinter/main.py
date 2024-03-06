from tkinter import *

window = Tk()

window.title("My first GUI Program")
window.minsize(500, 300)

#Label

my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")

# Button


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()


input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()