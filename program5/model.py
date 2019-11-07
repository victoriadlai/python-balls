import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from mobilesimulton import Mobile_Simulton
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0;
simulation  = set();
button      = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())


#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simulation,button
    running     = False;
    cycle_count = 0;
    simulation  = set()
    button      = None


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running
    global cycle_count
    running = True
    if running:
        cycle_count += 1
        for element in simulation.copy():
            element.update(model)
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global button
    button = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if button == 'Ball':
        simulation.add(Ball(x,y))
    elif button == 'Floater':
        simulation.add(Floater(x,y))
    elif button == 'Black_Hole':
        simulation.add(Black_Hole(x,y))
    elif button == 'Pulsator':
        simulation.add(Pulsator(x,y))
    elif button == 'Hunter':
        simulation.add(Hunter(x,y))
    elif button == 'Special':
        simulation.add(Special(x,y))
    elif button == 'Remove':
        for i in simulation.copy():
            if i.distance((x,y)) < i.radius:
                remove(i)
            
#add simulton s to the simulation
def add(s):
    simulation.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simulation.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    found = set()
    for i in simulation:
        if p(i):
            found.add(i)
    return found
    

#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for element in simulation.copy():
            element.update(model)


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for element in simulation:
        element.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(simulation))+" simultons/"+str(cycle_count)+" cycles")
