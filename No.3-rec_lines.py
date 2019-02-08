#CS2302  
#Tyler Salas  
#Lab1-No.3  
#Dr.Fuentes  
#Anindita Nath 
#Create Recursive Binary-Tree Figure

import numpy as np
import matplotlib.pyplot as plt 

#Recursive method modifies coordinates of new/next figures
def draw_squares(ax,n,p,w,length):
    if n>0:
        length1 = p[0,0] - p[2,0]
        length1 = length1 * -1
        length = (p[0,0]) - (p[2,0])
        length = (length//2)
        c1 = [[length//2,-500],[length,-500],[length*1.5,-500]]
        c2 = [[(length//2)+length1,-500],[length+length1,-500],[(length*1.5)+length1,-500]]
        q1 = p + c1
        q2 = p + c2 
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q1,w,length)
        draw_squares(ax,n-1,q2,w,length)
        

#Creates the three different figures
plt.close("all") 
orig_size = 800
p = np.array([[-300,-500],[0,0],[300,-500]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,.1,-600)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('lines.png')

plt.close("all") 
orig_size = 800
p = np.array([[-300,-500],[0,0],[300,-500]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,.1,-600)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('lines1.png')

plt.close("all") 
orig_size = 800
p = np.array([[-300,-500],[0,0],[300,-500]])
fig, ax = plt.subplots()
draw_squares(ax,6,p,.1,-600)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('lines2.png')
