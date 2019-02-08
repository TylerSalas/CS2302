#CS2302  
#Tyler Salas  
#Lab1-No.4
#Dr.Fuentes  
#Anindita Nath 
#Create Recursive Circle,Cross Figure

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


#Assigns new coordinates to new figure
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        c1 = [(radius*w)*2,0]
        c2 = [(radius*w)*2,0]
        c3 = [0,(radius*w)*2]
        c4 = [0,(radius*w)*2]
        i1 = np.array(center)+np.array(c1)
        i2 = np.array(center)-np.array(c2)
        i3 = np.array(center)+np.array(c3)
        i4 = np.array(center)-np.array(c4)
        #print(c1)
        #c1 = np.array(center) + np.array(q)
        #print(c1)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
        draw_circles(ax,n-1,i1,radius*w,w)
        draw_circles(ax,n-1,i2,radius*w,w)
        draw_circles(ax,n-1,i3,radius*w,w)
        draw_circles(ax,n-1,i4,radius*w,w)


#Creates the 3 different figures
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 3, [100,0], 100,.33)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles,cross.png')
        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 4, [100,0], 100,.33)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles,cross1.png')

plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 5, [100,0], 100,.33)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles,cross2.png')