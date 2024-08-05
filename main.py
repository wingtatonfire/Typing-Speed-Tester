from customtkinter import *
from ctypes import windll
import random


key = ""


# generate 3 lines of words for the text
# no more than 30 characters
with open("words_bank.txt", "r") as file:
    list_of_words = file.readlines()


def line_generate():
    line = ""
    for n in range(10):
        word = random.choice(list_of_words).strip("\n")
        line += word + " "
        if len(line) > 30:
            line = line.strip(word + " ")
            break
    return line


# timer for the 60s
def count_down(count):
    label_timer.configure(text=f"00:{count}")
    if count > 0:
        app.after(1000, count_down, count - 1)


def add_highlighter():
    label_text.tag_add("start", "1.11","1.17")
    label_text.tag_config("start", background= "black", foreground= "white")

def key_press(event):
    global key
    if event.char == " ":
        key = ""
        entry_text.delete(0, 'end')
    else:
        key += event.char
        print(key)
        return key

windll.shcore.SetProcessDpiAwareness(1)
app = CTk()
app.geometry("900x500")
xpad = 20
ypad = 10
font = ("aerial", 40)
app.title("Typing Wizard")

# mechanism
line1 = line_generate()
line2 = line_generate()
line3 = line_generate()


# layout
frame_text = CTkFrame(master=app, width=650)
frame_text.grid(column=0, row=1, padx=xpad, pady=50, columnspan=2)
frame_text.pack_propagate(0)

label_text = CTkLabel(master=frame_text, text=f"{line1}\n{line2}\n{line3}",
                      font=font, anchor="w", justify='left')
label_text.pack(anchor="w", expand=True, padx=xpad, pady=ypad)

entry_text = CTkEntry(master=app, placeholder_text="type the words here.", justify="center", font=("aerial", 40))
entry_text.grid(column=0, row=2, padx=xpad, pady=0, sticky="ew", columnspan=2)

button_start = CTkButton(master=app, text="Start", font=("aerial", 20), command=lambda: count_down(60))
button_start.grid(column=1, row=0, padx=xpad, pady=ypad, sticky="e")

label_timer = CTkLabel(master=app, text="01:00", font=font)
label_timer.grid(column=0, row=0, padx=xpad, pady=ypad, sticky="w")

#key
entry_text.bind('<Key>', key_press)


app.mainloop()

