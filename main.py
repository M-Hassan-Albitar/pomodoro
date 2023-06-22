import math
from tkinter import *

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
def reset_all():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    title_label.config(text="Timer")
    task_finish.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if reps in (1, 3, 5, 7):
    if reps % 2 == 0:
        count_down(work_sec)
        title_label.config(text="Work", foreground=RED)

    # elif reps in (2, 4, 6):
    elif reps % 3 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", foreground=PINK)

    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", foreground=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_in_min = math.floor(count / 60)
    count_in_sec = count % 60
    if count_in_sec == 0:
        count_in_sec = "00"
    elif count_in_sec < 10:
        count_in_sec = f"0{count_in_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_in_min}:{count_in_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        start_count()
        session = math.floor(reps / 2)
        for _ in range(session):
            mark += "✓"
            task_finish.config(text=mark, foreground=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=400, height=450)
window.title("Pomodoro")
window.config(bg=YELLOW)
window.resizable(FALSE, FALSE)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=205, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 100, image=tomato_img)
timer_txt = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1, pady=20, padx=20, sticky="w")

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), justify="center", bg=YELLOW, foreground=GREEN)
title_label.grid(row=0, column=1, pady=20)

start_btn = Button(text="Start", bg=PINK, foreground="white", font="bold", highlightthickness=0, command=start_count)
start_btn.grid(row=3, column=0, padx=20)

reset_btn = Button(text="Reset", bg=PINK, foreground="white", font="bold", highlightthickness=0, command=reset_all)
reset_btn.grid(row=3, column=2, padx=20)

task_finish = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW)
task_finish.grid(row=4, column=1)

window.mainloop()
