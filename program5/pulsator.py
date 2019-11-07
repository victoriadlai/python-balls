# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    time_between_meals = 0
    
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        self._counter_constant = 30
        
    def update(self, model):
        self.time_between_meals += 1
        eaten = Black_Hole.update(self,model)
        if len(eaten) > 0:
            for i in eaten.copy():
                self.change_dimension(1, 1)
                self.time_between_meals = 0
        else:
            if self.time_between_meals % self._counter_constant == 0:
                self.change_dimension(-1, -1)
                if self.get_dimension() == (0,0):
                    model.remove(self)
        return eaten
                    
