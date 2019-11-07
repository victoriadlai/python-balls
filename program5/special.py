# Creates a party with Special items that change color every 0.1 second, once
#    it is added into the simulation. Special behaves like a floater, however, 
#    it moves at 100 pixels/second, randomly switches it's angle 70% of the time, 
#    and does not change in speed.


from prey import Prey
import random


class Special(Prey):
    radius = 20
    count = 0
    
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self,x,y,width=self.radius*2,height=self.radius*2,angle=self.get_angle(),speed=100)
    
    def update(self,model):
        self.count += 1
        p = random.random()
        if p <= .69:
            a = self.get_angle() + (random.random()-0.5)
            self.set_angle(a)
        self.move()
        
    def display(self,canvas):
        possible_hex_digits = '0123456789abcdef'
        hex_color = '#'
        for i in range(6):
            hex_color += possible_hex_digits[random.randint(0,15)]

        canvas.create_oval(self._x-Special.radius, self._y-Special.radius,
                       self._x+Special.radius, self._y+Special.radius,
                       fill=hex_color)
        