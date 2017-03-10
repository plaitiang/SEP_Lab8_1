from turtle import *

class Disk:
    def __init__(self,x,y,h,w,c):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.c = c

    def showdisk(self):
        begin_fill()
        fd(self.w/2)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w/2)
        color(self.c)
        end_fill()
        color("black")

    def newpos(self,x,y):
        goto(x,y)

    def cleardisk(self):
        begin_fill()
        color("white")
        fd(self.w/2)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w)
        left(90)
        fd(self.h)
        left(90)
        fd(self.w/2)
        end_fill()
        color("black")
        
