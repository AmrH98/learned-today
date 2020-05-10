import tkinter as tk
import random

player1_score = 0
player2_score = 0
player1_ch = ""
player2_ch = ""

def ch_num(choice): #from char to num
    gain = {"rock":0,"paper":1,"scissor":2}
    return gain[choice]

def ch_char(choice): #from num to char
    gain = {0:"rock",1:"paper",2:"scissor"}
    return gain[choice]

def cpu_choice():
    return random.choice(['rock','paper','scissor'])

def score(pch,cch):
    global player1_score
    global player2_score
    user = ch_num(pch)
    cpu = ch_num(cch)
    if(user==cpu):
        print("Tie")
    elif((user-cpu)%3==1):
        print("You win")
        player1_score+=1
    else:
        print("Comp wins")
        player2_score+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)



window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300")

bstart = tk.Button(window, text="Start",bg="black")
bquit = tk.Button(window, text="Quit",bg="red")
bstart.grid(column = 4, row = 4,)
bquit.grid(column = 5, row = 4)
def rock():
    global player1_ch
    global player2_ch
    player1_ch= 'rock'
    player2_ch=random_computer_choice( )
    score( player1_ch , player2_ch )
def paper():
    global player1_ch
    global player2_ch
    player1_ch= 'paper'
    player2_ch=ch_num( )
    score( player1_ch , player2_ch )
def scissor():
    global player1_ch
    global player2_ch
    player1_ch= 'scissor'
    player2_ch=random_computer_choice( )
    result( player1_ch , player2_ch )

button1 = tk.Button(text="    Rock    ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="    Paper    ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="    Scissor    ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)


window.mainloop()


