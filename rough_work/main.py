# from tkinter import *
#
# window = Tk()
# window.title("Password Manager")
# window.config(padx=100, pady=100)
#
# canvas = Canvas(width=200, height=200)
# key_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=key_img)
# canvas.grid(column=1, row=0)
#
# website_entry = Entry(width=40)
# website_entry.grid(column=1, row=3)
# website_entry.focus()
#
#
# password_entry = Entry(width=35)
# password_entry.grid(column=1, row=1)
#
# email_entry = Entry(width=50)
# email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "ii_kayy@yahoo.com")
#
# website_label = Label(text="Website:", font=("italics", 10, "normal"))
# website_label.grid(column=0, row=1)
#
# email_label = Label(text="Email/Username:", font=("italics", 10, "normal"))
# email_label.grid(column=0, row=2)
#
# password_label = Label(text="Password:", font=("italics", 10, "normal"))
# password_label.grid(column=0, row=3)
#
# add_button = Button(text="Add", width=40)
# add_button.grid(column=1, row=4, columnspan=2)
#
# generate_password = Button(text="Generate Password")
# generate_password.grid(column=2, row=3)
#
# search_button = Button(text="Search", width=15)
# search_button.grid(column=2, row=2)
# window.mainloop()

import requests
from pprint import pprint
flight_ENDPOINT = "https://api.tequila.kiwi.com/"
flight_API_KEY = "biv_YloeSGsT_xHiKwYM-YgUkwAcPGH4"
sheet_ENDPOINT = "https://api.sheety.co/9c878535945b55a2d9735e35783b403d/flightDeals/prices"


response = requests.get(sheet_ENDPOINT)
result = response.json()
pprint(result)
sheet_data = result["prices"]
