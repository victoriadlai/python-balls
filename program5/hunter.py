# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        self.randomize_angle()
        w,h = self.get_dimension()
        Mobile_Simulton.__init__(self, x, y, width=w, height=h, angle=self.get_angle(), speed=5)
        self._distance_constant = 200
    
    def update(self,model):
        p = lambda sim: (isinstance(sim,Prey) and self.distance(sim.get_location()) <= 200)
        hunt = model.find(p)
        s_hunt = sorted(hunt.copy(), key=lambda x: self.distance(x.get_location()))
        if len(s_hunt) > 0:
            closest = s_hunt[0]
            cx,cy = closest.get_location()
            dif_x = cx - self._x
            dif_y = cy - self._y
            new_angle = atan2(dif_y,dif_x)
            self.set_angle(new_angle)
        Pulsator.update(self,model)
        self.move()
            
                
#         sorted_hunt = sorted(hunt,key=lambda hunt: (self.distance(i.get_location()) for i in hunt))
#         print(sorted_hunt)
#         if len(hunt) > 0:
#             new_angle = 
