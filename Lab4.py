# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019
import math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
# Gets the number of items in the list
def itemsAtDepth(T,d):
    count = 0
    #Gettnig the number of items in the first 
    if d == 0:
        #Case if d is 0
        return len(T.item)
    if T.isLeaf:
        #Case if T is a leaf
        count += len(T.item)
    elif d == 1:
        #Case if d is 1
        for i in range (len(T.child)):
            count += len(T.child[i].item)
    else:
        #Case if d is greater than 0 or 1
        for i in range (len(T.child)):
            count += itemsAtDepth(T.child[i],d-1) 
    return count

# No.1 Computes height of the tree by moving down the left side of the tree since all leaf nodes must be at same height
def computeHeight(T):
    if T.isLeaf:
        return 0
    return 1 + computeHeight(T.child[0])

# No.2 Creates sorted list by traversing through the list in order and appending elements along the way
def tree2List(T):
    lst = []
    if T.isLeaf:
        for t in T.item:
            lst.append(t)
    else:
        # For loop to add child elements
        for i in range(len(T.child)):
            lst += tree2List(T.child[i])
            # If statement to check if i is in range of item
            if i < len(T.item):
                lst.append(T.item[i])            
    return lst

# No.3 Returns the minimum element at depth d of the tree, returns -inf if the d is not a present depth in the tree
def minAtDepth(T,d):
    #Base case once depth d is found
    if d==0:
        return T.item[0]
    #Return statement if d is not in tree
    if T.isLeaf:
        return float('-inf')
    return minAtDepth(T.child[0],d-1)  

# No.4 Returns the maximum element at depth d of the tree, returns -inf if the d is not a present depth in the tree
def maxAtDepth(T,d):
    #Base case once depth d is found
    if d==0:
        return T.item[-1]
    #Return statement if d is not in tree
    if T.isLeaf:
        return float('-inf')
    return maxAtDepth(T.child[-1],d-1) 

# No.5 Returns the number of nodes at given depth d, returning -inf if d is not in the tree
def nodesAtDepth(T,d):
    count = 0
    if d == 0:
        #Case if d is 0
        return 1
    if T.isLeaf:
        #Case if T is a leaf
        return float('-inf')
    elif d == 1:
        #Case if d is 1
        count += len(T.child)
    else:
        #Case if d is greater than 0 or 1
        for i in range (len(T.child)):
            count += nodesAtDepth(T.child[i],d-1) 
    return count 

# Np.6 Prints all the items in the given depth d, returns none if d is not present
def printAtDepth(T,d):
    #Getting the number of items in the first  
    if d == 0:
        #Case if d is 0
        if T.item is not None:
            print(T.item)
            return
    if T.isLeaf:
        #Case if T is a leaf and d is out of bounds
        return float('-inf')
    elif d == 1:
        #Case if d is 1 will print the children of 0
        for i in range (len(T.child)):
            if T.child[i].item is not None:
                print(T.child[i].item,end='')
        return
    else:
        #Case if d is greater than 0 or 1
        for i in range (len(T.child)):
            if T.child[i] is not None:
                printAtDepth(T.child[i],d-1)
        return

# No.7 Will Return the Number of Full Nodes in the B-Tree
def fullNodes(T):
    count = 0
    # Case if T is only a leaf, will return 1 if full
    if T.isLeaf:
        if T.max_items == len(T.item):
            return 1
    # Case if T is not just a leaf will initially check root node
    if T.max_items == len(T.item):
        count += 1
    # After basic Node is checked will iterate through all of T's children
    for i in range(len(T.child)):
        count += fullNodes(T.child[i])
    return count

# No.8 will return the Number of full leaves in a B-Tree
def fullLeaves(T):
    count = 0
    # Case if node is a leaf and will only add to count if so
    if T.isLeaf:
        if T.max_items == len(T.item):
            return 1
    # Tracks all iterations of leaves to add them together
    for i in range(len(T.child)):
        count += fullLeaves(T.child[i])
    return count


# No.9 will return d, the depth at which an item being searched for can be found, returning -1 if not in the tree
def searchDepth(T,k,d):
    # Base case that will stop the search at and return depth d if item is in this depth
    if k in T.item:
        return d
    # Case if the key is not in the tree
    if T.isLeaf:
        return -1
    return searchDepth(T.child[FindChild(T,k)],k,d+1)

    



    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6, 102, 103, 104, 106, 107,91 ,92, 93, 94, 108, 109,7 ,8]
T = BTree()    
for i in L:
    Insert(T,i)
    #Print(T)
print("Displaying B-Tree:")
PrintD(T,' ')
print()

# No.1 Computes Height of Tree
print("Computing height of B-Tree: ",end='')
print(computeHeight(T))
print()


# No.2 Creates A Sorted List From Tree
print("Making Sorted List From Tree:")
print(tree2List(T))
print()


# No.3 Finds minimum at depth d, returning -inf if depth d is not in the tree
d = 1
print("The Minimum At Depth",d,": ",end='')
print(minAtDepth(T,d))
print()

# No.4 Finds maximum at depth d, returning -inf if depth d is not in the tree
de = 2
print("The Maximum At Depth",de,": ",end='')
print(maxAtDepth(T,de))
print()


# No.5 Finds the number of nodes at depth d, returning -inf if depth d is not in the tree
de = 2
print("Number of nodes At Depth",de,": ",end='')
print(nodesAtDepth(T,de))
print()

# No.6 prints the items at a given depth and will print None and nothing else if element is out of bounds
de = 2
print("Items At Depth",de,": ",end='')
print(printAtDepth(T,de))
print()


# No.7 Will return the number of full nodes in a B-Tree
print("Number of full nodes in T: ",end='')
print(fullNodes(T))
print()

# No.8 Will return the number of leaf nodes that are full in a B-Tree
print("Number of full leaves in T: ",end='')
print(fullLeaves(T))
print()


# No.9 Will return the depth at which a key k can be found, will return -1 if k is not in the B-Tree
k = 105
print("Searching for item: ",k)
print("Item found at depth ",end='')
print(searchDepth(T,k,0))
