from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
new_dict = {}

# Functionality

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")


words = data.to_dict(orient="records")


# Saving Progress
def is_known():
    global words
    words.remove(new_dict)
    new_data = pandas.DataFrame(words)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# What happens if the right button or wrong button is clicked
def next_card():
    global new_dict, flip_timer
    window.after_cancel(flip_timer)
    new_dict = random.choice(words)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(front_text, text="French", fill="black")
    canvas.itemconfig(front_text_2, text=new_dict["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# Translates the French word to English
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(front_text, text="English", fill="white")
    canvas.itemconfig(front_text_2, text=new_dict["English"], fill="white")


# Creating the UI
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
front_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
front_text_2 = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
