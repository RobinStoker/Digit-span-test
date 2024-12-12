from tkinter import *

MILLISECOND_BETWEEN = 2000

FONT_SIZE = 350
FONT = 'Helvetica'
FONT_STYLE = (FONT, FONT_SIZE)

BACKGROUND_COLOR = "black"
FOREGROUND_COLOR = "white"

RUN_KEY = '<Return>'


def startup(digits):
    def change_label(label, digit):
        label.config(text=digit)

    win = Tk()

    win.configure(background=BACKGROUND_COLOR)

    win.attributes('-fullscreen', True)
    win.attributes("-topmost", True)

    digit_label = Label(win, text="", font=FONT_STYLE)
    digit_label.config(foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR)
    digit_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def run_test(event):
        exec_after = 0
        for y, digit in enumerate(list(digits.digit_lists.values())[0]):
            exec_after += MILLISECOND_BETWEEN
            win.after(exec_after, change_label, digit_label, digit)
        exec_after += MILLISECOND_BETWEEN
        win.after(exec_after, change_label, digit_label, "")
        del digits.digit_lists[list(digits.digit_lists.keys())[0]]

    def test_over(event):
        win.destroy()

    win.bind(RUN_KEY, run_test)
    win.bind('<Escape>', test_over)

    win.mainloop()
