#CS2302  
#Tyler Salas  
#Lab6
#Dr.Fuentes  
#Anindita Nath 
#Create Mazes Using Disjoint Set Forests

import matplotlib.pyplot as plt
import numpy as np
import random

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i):
    if S[i] <= 0:
        return i
    s = i
    while S[i] >= 0:
         i = S[i]     
    root = i
    while S[s] >= 0:
        p = S[s]
        S[s] = root
        s = p
    return root


def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find_c(S,i) 
    rj = find_c(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                #ax.text((c+.5),(r+.5), str(cell), size=10,
                 #       ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def moreOneSet(S):
    count = 0
    for i in range(len(S)):
        if S[i] < 0:
            count += 1
    if count > 1:
            return True
    return False
    
def sameSet(S,i,j):
    i = find_c(S,i)
    #print(i)
    j = find_c(S,j)
    #print(j)
    if i == j:
        return True
    return False

plt.close("all") 
maze_rows = 10
maze_cols = 15


walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)

while moreOneSet(S):
    c1 = random.randint(0,len(walls)-1)
    if find(S,walls[c1][0]) != find(S,walls[c1][1]):
        union(S,walls[c1][0],walls[c1][1])
        walls.pop(c1)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 