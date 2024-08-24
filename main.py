from tkinter import *
import csv
import random


BACKGROUND_COLOR = "#B1DDC6"
card_index = 0

with open("french_words.csv", mode="r") as file:
    reader = csv.reader(file)
    word_list = list(reader)
print(word_list)


#----------------------------------------------------SHOWING CARDS-----------------------------------------------------#
def delete_word():
    word_list.pop(card_index)
    with open("french_words.csv", mode="w", newline='') as word_file:
        writer = csv.writer(word_file)
        writer.writerows(word_list)
    show_front()


def show_front():
    global card_index
    card_index = random.randint(0, len(word_list)-1)
    title_label.config(text=f"{word_list[card_index][0]}")
    word_label.config(text=f"???")
    window.after(3000, show_back)


def show_back():
    if len(word_list) > 0:
        title_label.config(text=f"{word_list[card_index][0]}")
        word_label.config(text=f"{word_list[card_index][1]}")


#----------------------------------------------------------UI----------------------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.minsize(800, 526)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

title_label = Label(canvas, text="", bg="white", font=('Arial', 40, 'italic'))
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

word_label = Label(canvas, text="Press ✅ when ready", bg="white", font=('Arial', 40, "bold"))
word_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

canvas.create_window(400, 150, window=title_label)
canvas.create_window(400, 263, window=word_label)

right_image = PhotoImage(file="right.png")
right_button = Button(window, image=right_image, command=show_front, highlightthickness=0, padx=20, pady=20)
right_button.grid(row=2, column=0)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(window, image=wrong_image, command=delete_word, highlightthickness=0, padx=20, pady=20)
wrong_button.grid(row=2, column=1)

window.mainloop()
