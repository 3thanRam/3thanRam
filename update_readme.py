import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import os

def main():
    Figure = plt.figure()
    
    # creating a plot
    lines_plotted = plt.plot([])     
    line_plotted = lines_plotted[0]
    
    plt.xlim(0,2*np.pi)  
    plt.ylim(-1.1,1.1)    
    
    # initialising x from 0 to 2∏
    x = np.linspace(0,2*np.pi,100)   
    #initially
    y = 0

    # function takes frame as an input
    def AnimationFunction(frame): 
    
        # setting y according to frame
        # number and + x. It's logic
        y = np.cos(x+2*np.pi*frame/100) 
    
        # line is set with new values of x and y
        line_plotted.set_data((x, y))
    
    anim_created = FuncAnimation(Figure, AnimationFunction, frames=100, interval=25)

    path=os.path.dirname(os.path.abspath(__file__))
    anim_created.save(filename=path+"/animation.gif", writer="pillow")
    plt.close()

if __name__ == "__main__":
    main()