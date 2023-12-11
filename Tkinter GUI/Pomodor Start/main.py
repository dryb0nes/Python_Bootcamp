from tkinter import *
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
    # remove checkmarks
    # reset time to quad 0's
    # Change header back to "timer"
    # stop timer

reset = False

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer) # type: ignore
    check_mark.configure(text="")
    timer_label.configure(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.configure(text="Break", fg=RED)
        count_down(l_break_sec)
    elif reps % 2 == 0:
        timer_label.configure(text="Break", fg=PINK)
        count_down(s_break_sec)
    else:
        timer_label.configure(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.configure(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Tkinter GUI\\Pomodor Start\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
start_bttn = Button(text="Start", command=start_timer)
reset_bttn = Button(text="reset", command=reset_timer)


# Grid layout
canvas.grid(column=1, row=1)
timer_label.grid(column=1, row=0,sticky="s")
start_bttn.grid(column=0, row=2, sticky="e")
reset_bttn.grid(column=2, row=2, sticky="w")
check_mark.grid(column=1, row=3)

window.mainloop()