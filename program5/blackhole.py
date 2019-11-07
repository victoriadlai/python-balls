# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, width=self.radius*2,height=self.radius*2)
    
    def update(self,model):
        found = model.find(self.contains)
        eaten = set()
        for i in found:
            if isinstance(i,Prey):
                eaten.add(i)
                model.remove(i)
        return eaten
    
    def display(self,canvas):
        w,h = self.get_dimension()
        canvas.create_oval(self._x-w/2, self._y-h/2,
                           self._x+w/2, self._y+h/2,
                           fill='black')
    
    def contains(self,s):
        return isinstance(s,Prey) and (self.distance(s.get_location()) < self._width/2)
            