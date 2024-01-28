import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.collections import EllipseCollection
import matplotlib.pyplot as plt
dt=0.02
g=10

def bounceball(Nballs,Lmin,Lmax):
    figsize=4
    Nframes=200
    Traillength=20
    fps=40

    Mid=(Lmax-Lmin)/2
    Circleradius=0.95*Mid
    center=np.array([Mid,Mid])
    R=(2*np.random.rand(2, Nballs)-1)*(Circleradius-3)*np.sqrt(2)/2+Mid 
    V=6*np.random.rand(2, Nballs)
    size = 0.5 +2*np.random.rand(Nballs)
    color = np.random.rand(Nballs)


    fig, ax = plt.subplots(figsize=(figsize, figsize))
    ax.set_facecolor((13/255,17/255,23/255))
    ax.set_xlim(Lmin,Lmax)
    ax.set_ylim(Lmin,Lmax)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    circle = plt.Circle(center, Circleradius,linewidth=3, color='grey',fill=False)
    ax.add_patch(circle)
    
    trail_positions = np.array([[R[dim, i] * np.ones(Traillength) for i in range(Nballs)] for dim in range(2)])
    
    widths=np.ones(Nballs*Traillength)
    widths[(np.arange(Nballs*Traillength)+1)%Traillength==0]=4

    fullsize=np.zeros(Nballs*Traillength)
    fullcolor=np.zeros(Nballs*Traillength)
    for n in range(Nballs):
        fullcolor[n*Traillength:(n+1)*Traillength]=color[n]
        fullsize[n*Traillength:(n+1)*Traillength]=size[n]*(Traillength-np.arange(Traillength))/Traillength
    


    
    pen=EllipseCollection(widths=fullsize, heights=fullsize,linewidths=widths,angles=np.zeros_like(fullsize),offsets=[],units="xy",facecolors=plt.cm.hsv(fullcolor),edgecolors="black",transOffset=ax.transData,)
    ax.add_collection(pen)
    def outbounds(arr, centerpos):
        return [ i for i in range(arr.shape[1]) if np.sqrt((arr[0,i]-centerpos[0])**2 + (arr[1,i]-centerpos[1])**2)>=Circleradius-0.5*size[i]]
    
    def animate(frame):
        R[0]+= V[0]*dt
        R[1]+= V[1]*dt-0.5*g*dt*dt
        V[1]-=g*dt
        for ind in outbounds(R,center):
            theta=np.arctan2(R[1,ind]-center[1],R[0,ind]-center[0])
            Vnorm=np.linalg.norm(V[:,ind])
            R[:,ind]=np.array([center[0]+(Circleradius-0.5*size[ind])*np.cos(theta),center[1]+(Circleradius-0.5*size[ind])*np.sin(theta)])
            V[:,ind]=np.array([Vnorm*np.cos(theta+np.pi),Vnorm*np.sin(theta+np.pi)])
        
        
        
        for i in range(Nballs):
            trail_positions[0,i]=np.roll(trail_positions[0,i],-1)
            trail_positions[1,i]=np.roll(trail_positions[1,i],-1)

            trail_positions[0,i,-1]=R[0, i]
            trail_positions[1,i,-1]=R[1, i]


        fullXoff,fullYoff=[],[]
        for b in range(Nballs):
            fullXoff+=[*trail_positions[0,b,:]]
            fullYoff+=[*trail_positions[1,b,:]]
        pen.set_offsets(np.c_[fullXoff,fullYoff])   
        return pen,

    anim_created = FuncAnimation(fig, animate, frames=Nframes, blit=False)
    anim_created.save(filename="./animation.gif",fps=fps, writer="pillow")

if __name__ == "__main__":
    bounceball(20,0,15)
    