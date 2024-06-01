import tkinter as tk
import random
window = tk.Tk()
window.geometry("900x500")
window.title("Rock Paper Scissors")
label = tk.Label(window,text="Choose one of the options",font=('Arial',20))
label.pack(pady=25)
button_frame = tk.Frame(window)
button_frame.pack()
button_height = 110
button_width = 220
paper_width = 30
paper_height = 7
papier = tk.PhotoImage(file="page.png")
papiera = papier.subsample(20,20)
sci = tk.PhotoImage(file="sc.png")
sc = sci.subsample(20,20)
roc = tk.PhotoImage(file="rock.png")
rocki = roc.subsample(100,100)
label2 = tk.Label(window,text="Computer = ???",font=('Arial',20))
label2.pack(pady=15)
label1 = tk.Label(window,text="vs",font=('Arial',20))
label1.pack(pady=17)
label3 = tk.Label(window,text="You = ???",font=('Arial',20))
label3.pack(pady=20)
R = 0
P = 0
S = 0
comp_R = 0
comp_P = 0
comp_S = 0
def rock_command():
    global R
    R = R+1
    label3.config(text="You = rock",image=rocki)
    confirm.config(state=tk.NORMAL)
def paper_command():
    global P
    P = P+1
    label3.config(text="You = paper",image=papiera)
    confirm.config(state=tk.NORMAL)
def scissors_command():
    global S
    S = S+1
    label3.config(text="You = scissors",image=sc)
    confirm.config(state=tk.NORMAL)
def computer():
    choices = ['P','R','S']
    comp = random.choice(choices)
    if comp == 'P':
        global P
        global comp_P
        P = P+1
        comp_P = comp_P+1
        label2.config(text="Computer = paper",image=papiera)
    elif comp == 'R':
        global R
        global comp_R
        R = R+1
        comp_R = comp_R+1
        label2.config(text="Computer = rock",image=rocki)
    elif comp == 'S':
        global S
        global comp_S
        S = S+1
        comp_S = comp_S+1
        label2.config(text="Computer = scissors",image=sc)
def result():
    if R == 1 and P == 1 and S == 1:
        label.config(text="Choose something")
    if R == 2 or P == 2 or S == 2:
        label.config(text='Draw')
        label2.config(bg="yellow")
        label3.config(bg="yellow")
    elif comp_R == 1 and P == 1:
        label.config(text="You win 🎉")
        label3.config(bg="Green")
        label2.config(bg="red")
    elif comp_R == 1 and S == 1:
        label.config(text="Computer wins")
        label2.config(bg="Green")
        label3.config(bg="red")
    elif comp_P == 1 and R == 1:
        label.config(text="Computer wins")
        label2.config(bg="Green")
        label3.config(bg="red")
    elif comp_P == 1 and S == 1:
        label.config(text="You win 🎉")
        label3.config(bg="Green")
        label2.config(bg="red")
    elif comp_S ==1 and R == 1:
        label.config(text="You win 🎉")
        label3.config(bg="Green")
        label2.config(bg="red")
    elif comp_S == 1 and P ==1:
        label.config(text="Computer wins")
        label2.config(bg="Green")
        label3.config(bg="red")
    re.config(state=tk.NORMAL)
    confirm.config(state=tk.DISABLED)
def reset():
    label.config(text="Choose one of the options")
    global R
    global S
    global P
    global comp_P
    global comp_S
    global comp_R
    R = 0
    P = 0
    S = 0
    comp_P = 0
    comp_S = 0
    comp_R = 0
    label2.config(text="Computer = ???",image='',bg='white')
    label3.config(text="You = ???",image='',bg='white')
    confirm.config(state=tk.NORMAL)
    re.config(state=tk.DISABLED)
def confir():
    computer()
    result()
rock = tk.Button(button_frame,text="Rock ",image=rocki,compound=tk.RIGHT,height=button_height,width=button_width,command=rock_command)
rock.pack(side=tk.LEFT,padx=10)
paper = tk.Button(button_frame,text="Paper",image=papiera,compound=tk.RIGHT,height=button_height,width=button_width,command=paper_command)
paper.pack(side=tk.LEFT,padx=10)
scissors = tk.Button(button_frame,text="Scissors",image=sc,compound=tk.RIGHT,height=button_height,width=button_width,command=scissors_command)
scissors.pack(side=tk.LEFT,padx=10)
confirm = tk.Button(button_frame, text="Confirm", command=confir)
confirm.pack()
re = tk.Button(button_frame, text="Reset", command=reset, state=tk.DISABLED)
re.pack()
window.mainloop()