from tkinter import *


import pygame
import math
from queue import PriorityQueue
import random
from tkinter import *



WIDTH = 1530
Height = 810

############## GUIDE #######################

root1= Tk()
root1.geometry("1000x700")
root1.title('Guide')

def get():
	root1.destroy()

label_0 =Label(root1,text="Beeline Perceiver",width=20,font=("bold",40))
label_0.place(x=200,y=40)

label_5=Label(root1,text="Quick Guide",width=20,font=(20))
label_5.place(x=380,y=110)

label_1=Label(root1,text="Controls",width=20,font=(20))
label_1.place(x=380,y=150)

label_2=Label(root1,text="1. Select any Combinations of Algorithm,obstacle percentage,direction in the next window.\n",font=(10))
label_2.place(x=50,y=180)

label_3=Label(root1,text="2. After Reaching the board Select Starting and Ending Node by Left Click of the Mouse.\n",font=(10))
label_3.place(x=50,y=220)
label_8=Label(root1,text="      You can unselect them by clicking on the same Node using Right Click.\n",font=(10))
label_8.place(x=50,y=260)

label_4=Label(root1,text="3. Once selecting those 2 points one can select any Node as an obstacle apart from Start and End Node.\n",font=(10))
label_4.place(x=50,y=300)
label_5=Label(root1,text="4. To Start The Algorithm, Press Space Bar!!!!.\n",font=(10))
label_5.place(x=50,y=340)
label_6=Label(root1,text="5. One Can Rerun the same Algorithm using the same Space Bar(Only after exection of the Algorithm).\n",font=(10))
label_6.place(x=50,y=380)
label_7=Label(root1,text="6. Press Ctrl+C to clear all the obstacle this will clear the entire Board including Start and End Node.\n",font=(10))
label_7.place(x=50,y=420)

Button(root1, text='Skip Guide...):' ,font=(20),width=20,bg="black",fg='white',command=get).place(x=380,y=580)

root1.mainloop()