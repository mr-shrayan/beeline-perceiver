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

##################   CHOICES  ##################


root = Tk()

root.geometry("500x500")

root.title('Alley Vizualizer')

entry_4 = StringVar()
entry_1 = StringVar()
entry_3 = StringVar()


def getinfo():
    main(entry_4.get(),entry_1.get(),entry_3.get())

label_0 =Label(root,text="Select your Choices",width=20,font=("bold",30))
label_0.place(x=20,y=40)

label_5=Label(root,text="Algorithms",width=20,font=("bold",10))
label_5.place(x=40,y=130)

Algorithms =[
        "Breadth First Search",
        "A*",
        "Dijikstra's",
        "Best First Search",
        "Swarm Algorithm",
        "Convergent Swarm Algorithm",
        "Bidirectional Swarm Algorithm"]



droplist=OptionMenu(root,entry_4, *Algorithms)

droplist.config(width=25)

entry_4.set('Select Any Algorithm...')
droplist.place(x=240,y=130)

label_1 =Label(root,text="Diagnol Neighbors", width=20,font=("bold",10))
label_1.place(x=40,y=280)

diagnol=["yes","no"]
    
option3=OptionMenu(root,entry_3,*diagnol)
option3.place(x=240,y=280)

entry_3.set('Choose Yes or No')
option3.config(width=15)

label_1 =Label(root,text="Obstracle percentage", width=20,font=("bold",10))
label_1.place(x=40,y=200)

Obstacleper =["0%","10%","20%","30%","40%","50%","100%"]
    
    #temp.set(Obstracleper[0])
option2=OptionMenu(root,entry_1,*Obstacleper)
option2.config(width=25)


entry_1.set('Choose Obstacle percentage')
option2.place(x=240,y=200)


#Checkbutton(root,text="Female", variable=var2).place(x=290,y=330)

Button(root, text='Submit' , width=20,bg="black",fg='white',command=getinfo).place(x=180,y=380)


yel=(242, 227, 7)
bl=(112,205, 226)
blu=(0, 172, 205)
RED = (190,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (181, 181, 22)
WHITE = (255, 255, 255)
BLACK = (60,60,60)
PURPLE = (128, 0, 128)
ORANGE = (201, 103, 170)
GREY = (128, 128, 128)
TURQUOISE = (15,135,0)


#CLASS

class Spot:
	def __init__(self, row, col,gap,gap1,width,height, total_rows,total_cols,diag):
		self.row = row
		self.col = col
		self.x = row * gap
		self.y = col * gap1
		self.color = WHITE
		self.neighbors = []
		self.diag=diag
		self.height=height
		self.width = width
		self.total_rows = total_rows
		self.total_cols = total_cols

        def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == RED

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = RED

	def make_closed(self):
		self.color = blu

	def make_open(self):
		self.color = bl

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = yel

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.y, self.x, self.width,self.height))

	def update_neighbors(self, grid):
		self.neighbors = []