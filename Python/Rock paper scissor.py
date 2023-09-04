from tkinter import *
from PIL import Image,ImageTk
from random import randint
#Tkinter is a GUI library (Tk interface)
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="black")

rock_img=ImageTk.PhotoImage(Image.open("rock_user.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper_user.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor_user.jpg"))
rockpc_img=ImageTk.PhotoImage(Image.open("rock_pc.jpg"))
paperpc_img=ImageTk.PhotoImage(Image.open("paper_pc.jpg"))
scissorpc_img=ImageTk.PhotoImage(Image.open("scissor_pc.jpg"))
#adding images
user_label=Label(root,image=scissor_img,bg='#9b59b6')
comp_label=Label(root,image=scissorpc_img,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)
#score
playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)
#indicatrs
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white").grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white").grid(row=0,column=1)

msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)
#update message
def updateMessage(x):
    msg['text']=x 
#update score
def updateuserscore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

def updatecomputerscore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)
choices=["rock","paper","scissor"]

#winner winner 
def checkingwinner(player,computer):
    if(player==computer):
        updateMessage("ITS A TIE!!")
    elif(player=="rock"):
        if(computer=="paper"):
            updateMessage("YOU LOOSE!!")
            updatecomputerscore()
        else:
            updateMessage("You WIN")
            updateuserscore()
    elif(player=="paper"):
        if(computer=="scissor"):
            updateMessage("YOU Loose!!")
            updatecomputerscore()
        else:
            updateMessage("You WIN")
            updateuserscore()
    elif(player=="scissor"):
        if(computer=="rock"):
            updateMessage("YOU Loose!!")
            updatecomputerscore()
        else:
            updateMessage("You WIN")
            updateuserscore()
    else:
        pass

def updatech(x):
    compchoice=choices[randint(0,2)]

    if(compchoice=="rock"):
        comp_label.configure(image=rockpc_img)
    elif(compchoice=="paper"):
        comp_label.configure(image=paperpc_img)
    else:
        comp_label.configure(image=scissorpc_img)
    #for user
    if(x=="rock"):
        user_label.configure(image=rock_img)
    elif(x=="paper"):
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkingwinner(x,compchoice)

#adding buttons here
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF6D33",fg="white",command=lambda:updatech("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#336FFF",fg="white",command=lambda:updatech("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#FF3367",fg="white",command=lambda:updatech("scissor")).grid(row=2,column=3)
root.mainloop()