from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = 'GREEN'
FOOD_COLOR = 'RED'
BG_COLOR = '#000000'

class Snake:
    pass

class Food:
    pass


def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass



window = Tk()
window.title('Snake Game')
window.resizable(False,False)

score = 0
direction = 'down'


label = Label(window,text='Score: {}'.format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window,bg=BG_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()


window.mainloop()