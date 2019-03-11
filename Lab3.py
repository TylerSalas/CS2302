#CS2302  
#Tyler Salas  
#Lab3 
#Dr.Fuentes  
#Anindita Nath 
#Implemnt Binary Tree Functions
import time
import matplotlib.pyplot as plt
import numpy as np
import math 


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def getHeight(T): 
    if T is None: 
        return 0 
    else: 
        leftHeight = getHeight(T.left) 
        rightHeight = getHeight(T.right) 
        if leftHeight > rightHeight : 
            return leftHeight+1
        else: 
            return rightHeight+1

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

#Searches for a node with while loop iterations (No.2)
def iterativeSearch(T,k):
    if T is None:
        return -1
    t = T
    while t is not None and t.item != k:
        if k < t.item:
            t = t.left
        else:
            t = t.right
    if t is None:
        return None
    else:
        if t is None:
            return -1
        return t

#Sorted List to a Tree (No.3)
def listToTree(T,l):
    if len(l) == 0:
        return None
    mid = len(l)//2
    if T is None:
        head = BST(l[mid])
    head.left = listToTree(T,l[:mid])
    head.right = listToTree(T,l[mid+1:])
    return head

#Tree To Sorted List (No.4)
def treeToList(T,l):
    if T is not None:
        treeToList(T.left,l)
        l.append(T.item)
        treeToList(T.right,l)

#(No.5)
#Iterates through all the levels to print each one using the printLevel function
def printLevels(T): 
    hgt = getHeight(T) 
    c = 0
    while c < hgt:
        print()
        print("Items At Level ",c, end='')
        print(": ")
        printLevel(T, c)
        c += 1

#Used by printLevels function to print a certain level given by n  
def printLevel(T,n): 
    if T is None: 
        return
    if n == 0: 
        print(T.item,end=' ')
    elif n > 0 : 
        printLevel(T.left ,n-1) 
        printLevel(T.right ,n-1)


def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#Visualizes tree
def draw_Branch(ax,T,p,w,length,rad):
    if T is not None:
        if T.left is None and T.right is None:
            center = [p[1,0],p[1,1]]
            x,y = circle(center,rad)
            ax.plot(x,y,color='k')
            ax.text(center[0]-60,center[1]-60,T.item,fontsize=15)
            return
        center = [p[1,0],p[1,1]]
        x,y = circle(center,rad)
        ax.plot(x,y,color='k')
        ax.text(center[0]-50,center[1]-60,T.item,fontsize=15)
        
        length1 = p[0,0] - p[2,0]
        length1 = length1 * -1
        length = (p[0,0]) - (p[2,0])
        length = (length//2)
        c1 = [[length//2,-500],[length,-500],[length*1.5,-500]]
        c2 = [[(length//2)+length1,-500],[length+length1,-500],[(length*1.5)+length1,-500]]
        q1 = p + c1
        q2 = p + c2 
        ax.plot(p[:,0],p[:,1],color='k')
        ax.plot(100,100)
        draw_Branch(ax,T.left,q1,w,length,rad)
        draw_Branch(ax,T.right,q2,w,length,rad)

def drawBranch1(ax,br,center,ang):
    br[0,0] = center[0] -20 + np.sin(ang)
    br[0,1] = center[1] -20 + np.cos(ang)
    ax.plot(br[:,0],br[:,1],color='k')
    return [br[0,0],br[0,1]]
        
#Code to visualize a tree               
z = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    z = Insert(z,a)  
   
start = time.time()
plt.close("all") 
fig, ax = plt.subplots() 
ax.axis('off')
ax.set_aspect(.50)
p = np.array([[-300,-500],[0,0],[300,-500]])
draw_Branch(ax,z,p,.1,-600,75)



# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)

#Test case No.2
print("Searching for item 45: ",end='')
it = iterativeSearch(T,45)
print(it.item)
print()

#Test case No.3
t = None
B = [1,2,3,4,5,6,7,8,9,10]
print("Making List ",B," into a tree")
b = listToTree(t,B)
InOrderD(b,' ')
print()

#test case No.4
E = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    E = Insert(E,a)
l = []
treeToList(E,l)
print("Making Tree To List: ")
print(l)
print()

#test case No.5
print("Printing Tree Levels Of T: ")
t = None
InOrderD(T,' ')
printLevels(T)

print()
print()
print("Binary Tree Visualized")  







