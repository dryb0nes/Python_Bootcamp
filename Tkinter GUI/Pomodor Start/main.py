from itertools import count
from tkinter import *
from tracemalloc import start
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Tkinter GUI\\Pomodor Start\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
timer_label = Label(text="Timer")
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
start_bttn = Button(text="Start", command=start_timer)
reset_bttn = Button(text="reset", command=reset_timer)


# Grid layout
canvas.grid(column=1, row=1)
timer_label.grid(column=1, row=0,sticky="s")
start_bttn.grid(column=0, row=2, sticky="e")
reset_bttn.grid(column=2, row=2, sticky="w")
check_mark.grid(column=1, row=3)



#Config Changes
timer_label.config(font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
window.mainloop()