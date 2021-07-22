import tkinter 
import random

# Vraiables
score=0
timer=60
word_color=""
reset=0

colors=["Black", "Blue", "Brown", "Cyan", "Green", "Magenta", "Orange", "Pink", "Purple", "Red", "White", "Yellow"]

# Functions
def start_timer():
    global timer, reset
    if timer>=0 and reset==0:
        time_label.config(text="Game Ends in : {}s".format(timer))
        timer=timer-1
        time_label.after(1000,start_timer)
        if timer==-1:
            time_label.config(text="Game Over!!!")

def next_word(event):
    global word_color, score
    if timer>0:
        if word_color==entry_box.get().lower():
            score=score+1
            score_label.config(text="Your Score: {}".format(str(score)))
        entry_box.delete(0,tkinter.END)
        word_color=random.choice(colors).lower()
        words_label.config(text=random.choice(colors),fg=word_color)


def start_game():
    global word_color, reset
    reset=0
    if(timer == 60):
        start_timer()
        word_color = random.choice(colors).lower()
        words_label.config(text=random.choice(colors), fg=word_color)
        # When enter key is pressed, it returns to next_word() function
        entry_box.bind("<Return>", next_word)

def reset_game():
    global timer, score, word_color, reset
    timer = 60
    score = 0
    word_color = ''
    reset=1
    score_label.config(text="Your Score: {}".format(str(score)))
    words_label.config(text='')
    time_label.config(text="Game Ends in : -")
    entry_box.delete(0, tkinter.END)


window=tkinter.Tk()

window.title("Color Game")
window.geometry("500x300")
window.resizable(False,False)
window.config(background="lavender")


# Create widgets
description="Enter the color of the words displayed below. \n Don't enter the word text itself"
description_frame=tkinter.Frame(window,bg="lavender")
description_frame.pack(side=tkinter.TOP)

description_label1=tkinter.Label(description_frame,text="Game Description:",font=('Helvetica',12,'bold'),fg="pink4", bg="lavender")
description_label1.grid(row=0,column=0)

description_label2=tkinter.Label(description_frame,text=description,font=('Helvetica',12),fg="pink4", bg="lavender")
description_label2.grid(row=0,column=1)

score_label=tkinter.Label(window,text="Your Score: {}".format(str(score)),font=('Helvetica',16,'bold'),fg="slateblue4",bg="lavender")
score_label.pack()

words_label=tkinter.Label(window,font=('Helvetica',28),pady=10,bg="lavender")
words_label.pack()

time_label=tkinter.Label(window, text = "Game Ends in: -", font=('Helvetica',16,'bold'), fg="slateblue4",bg="lavender")
time_label.pack()

entry_box=tkinter.Entry(window,width=30)
entry_box.pack(pady=10)

button_frame=tkinter.Frame(window, width=80, height=40, bg="black")
button_frame.pack(side=tkinter.BOTTOM)
# Divide the frame into two parts
start_button=tkinter.Button(button_frame, text ="Start", width=20, fg = "black", bg="pink", bd=0, padx=20, pady=10, command = start_game)
start_button.grid(row=0, column= 0)
reset_button=tkinter.Button(button_frame, text ="Reset", width=20, fg = "black", bg="light blue", bd=0, padx=20, pady=10, command = reset_game)
reset_button.grid(row=0, column=1)

window.mainloop()
