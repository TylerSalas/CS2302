#CS2302  
#Tyler Salas  
#Lab7
#Dr.Fuentes  
#Anindita Nath 
#Create Mazes and evaluate with graphs

import matplotlib.pyplot as plt
import numpy as np
import random
import time

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
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    fig.savefig('square.png')

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
    
def printPath(prev,v):
    if prev[v] != -1:
        printPath(prev,prev[v])
        print("-",end=' ')
    print(v,end=' ')

#Adds an element to an adjacency list
def addToList(L,x,y):
    L[x].append(y)
    L[y].append(x)
        
def breadthFirstSearch(G,v):
    visited = [False for i in range(len(G))]
    prev = [-1 for i in range(len(G))]
    Q = []
    Q.insert(0,v)
    visited[v] = True
    while len(Q) > 0:
        #print(Q)
        u = Q.pop()
        for t in G[u]:
            if visited[t] == False:
                visited[t] = True
                prev[t] = u
                Q.insert(0,t)
    return prev



def depthFirstSearch(G,v):
    visited = [False for i in range(len(G))]
    prev = [-1 for i in range(len(G))]
    Q = []
    Q.append(v)
    visited[v] = True
    while len(Q) > 0:
        #print(Q)
        u = Q.pop()
        for t in G[u]:
            if visited[t] == False:
                visited[t] = True
                prev[t] = u
                Q.append(t)
    return prev

def depthFirstSearchRec(G,v,visited,prev,Q):
    if not True in visited:
         Q = []
         Q.append(v)
         visited[v] = True
    if len(Q) > 0:
        u = Q.pop()
        for t in G[u]:
            if visited[t] == False:
                visited[t] = True
                prev[t] = u
                Q.append(t)
                depthFirstSearchRec(G,v,visited,prev,Q)





plt.close("all") 
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)
aList = [[] for i in range(maze_rows*maze_cols)]

'''
print("A path from source to destination is not guaranteed when m < ",(maze_rows*maze_cols)-1)
print("There is a uniqe path from source to destination when m = ",(maze_rows*maze_cols)-1)
print("There is at least one path from source to destination when m > ",(maze_rows*maze_cols)-1)
m = input("How many walls shall be popped: ")
m = int(m)
'''
m = (maze_rows*maze_cols)-1 
count = 0

#Builds maze
while moreOneSet(S) and count < m:
    c1 = random.randint(0,len(walls)-1)
    if find(S,walls[c1][0]) != find(S,walls[c1][1]):
        #Adds element to adjacency list representing graph
        addToList(aList,walls[c1][0],walls[c1][1])
        #uniting two components in the dsf
        union(S,walls[c1][0],walls[c1][1])
        #removing walls
        walls.pop(c1)
        #Adding to keep track of m
        count += 1
          
#Breadth First Search
start = time.time()
print("Breadth First Search: ")        
G = breadthFirstSearch(aList,0)
printPath(G,len(aList)-1)
end = time.time()
print()
print("Runtime: ",end-start)
print()



#Depth First Search
start = time.time()
print("Depth First Search: ")
G = depthFirstSearch(aList,0)
printPath(G,len(aList)-1)
end = time.time()
print()
print("Runtime: ",end-start)
print()

#Depth First Search With Recursion
start = time.time()
print("Depth First Search With Recursion: ")
visited = [False for i in range(len(aList))]
prev = [-1 for i in range(len(aList))]
Q = []
depthFirstSearchRec(aList,0,visited,prev,Q)
printPath(prev,len(aList)-1)
end = time.time()
print()
print("Runtime: ",end-start)
print()



draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
