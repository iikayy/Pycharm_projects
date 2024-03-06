from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_list = {}

try:
    words_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words_list = original_data.to_dict(orient="records")
else:
    words_list = words_df.to_dict(orient="records")
# print(words_list)


def random_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    french = current_card["French"]
    english = current_card["English"]
    canvas.itemconfig(title_text, text="French",fill="black")
    canvas.itemconfig(word_text, text=f"{french}",fill="black")
    canvas.itemconfig(old_image, image=front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"],fill="white")
    canvas.itemconfig(old_image, image=back_img)


def remove_card():
    words_list.remove(current_card)
    words_to_learn = pandas.DataFrame(words_list)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    random_card()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
old_image = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=x_img, highlightthickness=0, command=random_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=remove_card)
known_button.grid(column=1, row=1)

random_card()



window.mainloop()