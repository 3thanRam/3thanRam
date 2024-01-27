import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.collections import EllipseCollection
import matplotlib.pyplot as plt
dt=0.02
g=10

def Initvalues(N,Circleradius):
    R=Circleradius*np.random.rand(2, N)
    V=4*np.random.randn(2, N)
    size = 0.5 +2*np.random.rand(N)
    color = np.random.rand(N)
    return R,V,size,color

    
def bounceball(Nballs,Lmin,Lmax):
    figsize=6
    Nframes=500
    fps=40
    
    fig, ax = plt.subplots(figsize=(figsize, figsize))
    fig.patch.set_alpha(0.0)
    plt.rcParams['savefig.transparent'] = True
    ax.set_xlim(Lmin,Lmax)
    ax.set_ylim(Lmin,Lmax)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)


    Circleradius=(Lmax-Lmin)/2
    center=np.array([Circleradius,Circleradius])
    circle = plt.Circle(center, Circleradius,linewidth=3, color='black',fill=False)

    R,V,size,color = Initvalues(Nballs,Circleradius)

    ax.add_patch(circle)
    pen=EllipseCollection(widths=size, heights=size,linewidths=3,angles=np.zeros_like(size),offsets=[],units="xy",facecolors=plt.cm.hsv(color),edgecolors="black",transOffset=ax.transData,)
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

        pen.set_offsets(np.c_[R[0],R[1]])
        return pen,

    anim_created = FuncAnimation(fig, animate, frames=Nframes, blit=False)
    anim_created.save(filename="./animation.gif",fps=fps, writer="pillow",savefig_kwargs={'transparent': True})

if __name__ == "__main__":
    bounceball(15,0,15)
