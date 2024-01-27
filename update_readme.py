import numpy as np
from matplotlib.animation import FuncAnimation
import random
import matplotlib
import ffmpeg

import matplotlib.pyplot as plt
import os
dt=0.1
radius=0.5

def Random(Xbounds,Ybounds):
    x0,y0=random.uniform(*Xbounds),random.uniform(*Ybounds)
    vxmax,vymax=0.1*abs(Xbounds[1]-Xbounds[0])/dt,0.1*abs(Ybounds[1]-Ybounds[0])/dt
    vx0,vy0=vxmax*random.uniform(-1,1),vymax*random.uniform(-1,1)
    return x0,y0,vx0,vy0

def bounceball():
    figsize=6
    Nballs=25
    Xmin,Xmax=0,10
    Ymin,Ymax=0,10
    
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_xlim(Xmin,Xmax)
    ax.set_ylim(Ymin,Ymax)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    x,y,vx,vy=Random([Xmin,Xmax],[Ymin,Ymax])
    x, y = 5*(1+np.random.rand(2, Nballs))
    vx,vy=4*np.random.rand(2, Nballs)
    size = 0.6 +np.random.rand(Nballs)
    color = np.random.rand(100)

    pen=matplotlib.collections.EllipseCollection(widths=size, heights=size,angles=np.zeros_like(size),offsets=[],units="xy",facecolors=plt.cm.hsv(color),edgecolors="black",transOffset=ax.transData,)
    ax.add_collection(pen)
    
    def animate(frame):
        nonlocal x,y,vx,vy
        x += vx*dt
        y += vy*dt
        vx[x+radius>=Xmax]=abs(vx[x+radius>=Xmax])*(-1)
        vx[x-radius<=Xmin]=abs(vx[x-radius<=Xmin])
        x[x+radius>=Xmax]=Xmax-radius
        x[x-radius<=Xmin]=Xmin+radius

        vy[y+radius>=Ymax]=abs(vy[y+radius>=Ymax])*(-1)
        vy[y-radius<=Ymin]=abs(vy[y-radius<=Ymin])
        y[y+radius>=Ymax]=Ymax-radius
        y[y-radius<=Ymin]=Ymin+radius

        pen.set_offsets(np.c_[x, y])
        return pen,

    anim_created = FuncAnimation(fig, animate, frames=150, blit=True)
    path=os.path.dirname(os.path.abspath(__file__))
    anim_created.save(filename=path+"/animation.mp4",fps=25, writer="ffmpeg")
    
    forward = ffmpeg.input(path+'/animation.mp4')
    (
        ffmpeg
        .concat(
            forward,
            forward.filter('reverse'),
        )
        .output(path+'/animationfull.mp4')
        .run()
    )
    
    plt.close()

if __name__ == "__main__":
    bounceball()