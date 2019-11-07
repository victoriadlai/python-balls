# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self,x,y,width=self.radius*2,height=self.radius*2,angle=self.get_angle(),speed=5)
        
    def update(self,model):
        p = random()
        if p <= .29:
            s = self.get_speed() + (random()-0.5)
            a = self.get_angle() + (random()-0.5)
            if 3 <= s <= 7:
                self.set_speed(s)
            self.set_angle(a)
        self.move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                           self._x+Floater.radius, self._y+Floater.radius,
                           fill='red')