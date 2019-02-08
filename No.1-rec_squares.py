#CS2302  
#Tyler Salas  
#Lab1-No.1
#Dr.Fuentes  
#Anindita Nath 
#Create Recursive Squares Figure

import numpy as np
import matplotlib.pyplot as plt


#Recursive method to assign new coordinates to new/next figure
def draw_squares(ax,n,p,w,):
    if n>0:
        distance = p[0,0] - p[2,0]
        c1 = [[distance*w, distance*w],
              [distance*w, distance*(3*w)],
              [distance*(3*w), distance*(3*w)],
              [distance*(3*w), distance*w],
              [distance*w, distance*w]]
        c2 = [[distance*w, distance*(-3*w)],
               [distance*w, distance*(-1*w)],
               [distance*(3*w), distance*(-1*w)],
               [distance*(3*w), distance*(-3*w)],
               [distance*w, distance*(-3*w)]]
        c3 = [[distance*(-3*w), distance*(-3*w)],
               [distance*(-3*w), distance*(-1*w)],
               [distance*(-1*w), distance*(-1*w)],
               [distance*(-1*w), distance*(-3*w)],
               [distance*(-3*w), distance*(-3*w)]]
        c4 = [[distance*(-3*w), distance*(w)],
               [distance*(-3*w), distance*(3*w)],
               [distance*(-1*w), distance*(3*w)],
               [distance*(-1*w), distance*(w)],
               [distance*(-3*w), distance*(w)]]
        q1 = p + c1
        q2 = p + c2
        q3 = p + c3
        q4 = p + c4
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q1,w)
        draw_squares(ax,n-1,q2,w)
        draw_squares(ax,n-1,q3,w)
        draw_squares(ax,n-1,q4,w)

#Creates the 3 different figures
plt.close("all") 
orig_size = 1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')

plt.close("all") 
orig_size = 1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares1.png')

plt.close("all") 
orig_size = 1000
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,.25)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares2.png')
