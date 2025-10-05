from tkinter import *
from tkinter import messagebox
import math

FONT_NAME="Arial"
DARK_BLUE = "#3674B5"
BLUE='#578FCA'
WHITE= "#FFFFFF"
HIGHLIGHT = "#FFFD8C"

timer = None 
correct_count = 0
current_index = 0

def center_title(event):
    "Centers the title when the window expands"
    width = event.width
    height = event.height
    title_canvas.coords(title, width / 2, height / 2)  

def reset():
   "Resets the timer and score"
   window.after_cancel(timer)
   timer_canvas.itemconfig(timer_text, text="1:00")
   score_text.set('')
   word_input.delete(0, "end")
   word_input.bind('<Key>',start_timer)
   global correct_count
   global current_index
   correct_count = 0
   current_index = 0

def start_timer(_):
      "Starts the timer"
      count_down()
      word_input.unbind("<Key>")
      
def count_down(count=60):
      "Countdown from 1 minute"
      count_min = math.floor(count/60)
      count_sec = count%60
      if count_sec < 10:
            count_sec = f"0{count_sec}"
      timer_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
      if count>0:
            global timer
            timer = window.after(1000,count_down,count-1)
      else:
            global correct_count
            messagebox.showinfo(title='Result', message=f"Typing Speed: {correct_count} WPM")

def counter(_):
      "Updates the score"
      global correct_count
      global current_index
      if word_list[correct_count] == word_input.get().strip():
            correct_count +=1
            current_index += 1
            highlight(current_index)
            score_text.set(correct_count)
            word_input.delete(0, "end")

def highlight(index):
     "Highlights current word"
     words_text.tag_remove("highlight", "1.0","end")

     if index < len(word_list):
            start = "1.0"
            for i in range(index):
                  start = words_text.search(word_list[i],start,stopindex="end")
                  if not start:
                        return
                  start = f"{start}+{len(word_list[i]) +1}c"

            word = word_list[index]
            word_start = words_text.search(word,"1.0",stopindex="end")
            if word_start:
                  word_end = f"{word_start}+{len(word)}c"
                  words_text.tag_add("highlight", word_start, word_end)

words = "shadow harbor drift lantern prism canyon velvet orbit \
         \n whisper summit thunder meadow frost ladder engine \
         \n marble forest sketch horizon echo ribbon puzzle hat \
         \n desert feather compass stream mirror galaxy branch \
         \n planet tunnel crystal valley beacon jungle canvas \
         \n torch mountain pattern bridge meadow silver drift his\
         \n signal legend flame current voyage ripple marble me \
         \n horizon frost village ladder orchard orbit banner hear \
         \n comet canyon circuit rhythm spark anchor pink is\
         \n her mirror garden stripe orange village climb indigo"

word_list = [word for word in words.split(' ') if (word!='' and word!='\n')]

window=Tk()
window.minsize(width=700, height=750)
window.config(padx=10, pady=10, bg='white')
window.title('Typing Speed Test')
window.resizable(True, True) 

title_canvas = Canvas(window, bg=DARK_BLUE, height=50, borderwidth=0)
title = title_canvas.create_text(0,0,
                                text ="Typing Speed Test", 
                                fill="white", 
                                font=(FONT_NAME, 35, "bold"),
                                justify='center')
title_canvas.pack(fill=X)
title_canvas.bind("<Configure>", center_title)

instructions = Label(window, 
                     text="How fast can you type? Do the one-minute typing test to find out! \n Press the space bar after each word. At the end, you'll get your typing speed in CPM and WPM. \n Good luck!", 
                     pady=15,
                     font=(FONT_NAME,17,'bold'),
                     fg=DARK_BLUE,
                     bg=WHITE)
instructions.pack()

frame = Frame(window, bg=WHITE, width=500, height=35)
frame.pack(pady=5) 
frame.pack_propagate(False) 

score_text=StringVar()
score= Label(fg=DARK_BLUE, textvariable=score_text, font=(FONT_NAME, 25, "bold"), bg=WHITE)
score.pack(in_=frame, side='right')

timer_canvas = Canvas(width=65, height=30, bg=WHITE, borderwidth=0)
timer_text = timer_canvas.create_text(35,20,text="0:00",font=(FONT_NAME, 25, "bold"), fill=DARK_BLUE, justify='center')
timer_canvas.pack(in_=frame, side='left')

word_canvas = Canvas(window,
                     bg=WHITE,
                     height=250,
                     width=500)
word_canvas.pack()

words_text = Text(word_canvas,
                   font=(FONT_NAME,17),
                   fg='black',
                   wrap='word',
                   bg=WHITE,
                   borderwidth=0,
                   height=10,
                   width=40,
                   highlightthickness=0)
words_text.insert("1.0", words)
words_text.tag_add("center","1.0", "end")
words_text.tag_config("center", justify="center")
words_text.tag_config('highlight', background=HIGHLIGHT, foreground='black')
highlight(current_index)
words_text.config(state="disabled")

word_canvas.create_window(250,125, window=words_text, anchor='center')

word_input = Entry(highlightthickness=3,font=(FONT_NAME,17))
word_input.config(highlightbackground = BLUE, highlightcolor= BLUE)
word_input.bind('<Key>',start_timer)
word_input.bind('<KeyRelease-space>', counter)
word_input.pack(pady=15)

button_frame = Frame(window, bg=WHITE, width=5)
button_frame.pack()

start_button = Button(text="Start", 
                      highlightthickness=0, 
                      command=count_down, 
                      font=(FONT_NAME,15,"bold"),  
                      bg="white", 
                      fg=DARK_BLUE,
                      width=5, 
                      height=2)
start_button.pack(in_=button_frame, side=LEFT)

reset_button = Button(master=window,
                        text='Reset',
                        font=(FONT_NAME,15,'bold'), 
                        highlightthickness=0,
                        highlightcolor=WHITE,
                        bg=BLUE,  
                        width=5, height=2, 
                        command = reset)
reset_button.pack(in_=button_frame, side=LEFT, padx=5)
                        
window.mainloop()