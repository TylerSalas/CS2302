# Implementation of hash tables with chaining using strings
import numpy as np
import math
import time

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

#Returns position in alphabet
def char_position(letter):
    return ord(letter) - 97

#Returns true if item is to the left and false if it is to the right
def compElem(word1,word2):
    if word1 > word2:
        return True
    return False

#Converts List of sorted words into A Tree
def listToTree(T,A):
    if len(A) == 0:
        return None
    mid = len(A)//2
    if T is None:
        head = BST(A[mid])
    head.left = listToTree(T,A[:mid])
    head.right = listToTree(T,A[mid+1:])
    return head

#Returns the number of nodes in Given Tree
def numNodes(T):
    if T is None:
        return 0
    return 1 + numNodes(T.left) + numNodes(T.right)
     
#Returns Hieght of Given Tree   
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

#Finds A Node In A BST
def findB(T,k):
    if T is None:
        return -1
    if T.item[0] == k:
        return T.item
    cur = T.item[0]
    if compElem(cur,k):
        return findB(T.left,k)
    return findB(T.right,k)

#Calculates The Similarites Of Two Words In A Binary Search Tree
def compSim(T,word1,word2):
    #Declaring Two words To Work With
    word1 = findB(T,word1)
    word2 = findB(T,word2)
    #Finding Dot Product of Word Embeddings
    dp = dotProduct(word1,word2)
    #Finding Magnitudes of two words
    mag1 = Magnitude(word1)
    mag2 = Magnitude(word2)
    denom = mag1 * mag2
    return dp/denom

#Gets The Dot Product of Two Words from a Binary-Tree
def dotProduct(word1,word2):
    dp = 0
    for i in range(len(word1[1])):
        dp += word1[1][i] * word2[1][i]
    return dp

#Calculates the Magnitude Of A Word From A Binary-Tree
def Magnitude(word):
    mag = 0
    for i in range(len(word[1])):
        mag += word[1][i] * word[1][i]
    return math.sqrt(mag)


    
    
    


#Functions concerning hash tables
#------------------------------------------------------------------------------
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor

    def __init__(self,size,num_Items):  
        self.item = []
        self.size = size
        self.num_Items = 0
        for i in range(size):
            self.item.append([])

def NumItems(H):
    count = 0
    for i in range(len(H.item)):
        count += len(H.item[i])
    return count    
    
def LoadFac(H):
    count = 0
    for i in range(len(H.item)):
        count += len(H.item[i])
    num_Items = count
    return num_Items/len(H.item)
        
def InsertC(H,k,l,e):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([e]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0][0] == k:
            return H.item[b][i]
    return -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c)) % n
    return r

#Turns list with words and embeddings into a Hash-Table
def crtHT(A):
    H = HashTableC(11,0)
    for i in range(len(A)):
        #inserting elements into Hash-Table
        elem = [A[i][0],A[i][1]]
        InsertC(H,elem[0],len(elem[0]),elem)
        H.num_Items += 1
        #Checks if load factor is = 1 and if so makes list size larger by *2+1
        if(H.num_Items == H.size):
            for i in range(H.size+1):
                H.item.append([])
            H.size = (H.size*2)+1
        
    return H

#Gets The Dot Product of Two Words in A Hash-Table
def dotProductH(word1,word2):
    dp = 0
    for i in range(len(word1[1])):
        dp += word1[1][i] * word2[1][i]
    return dp

#Calculates the Magnitude Of A Word In A Hash-Table
def MagnitudeH(word):
    mag = 0
    for i in range(len(word[1])):
        mag += word[1][i] * word[1][i]
    return math.sqrt(mag)

#Compares Similarities In A Hash-Table
def compSimH(H,word1,word2):
    #Declaring Two Words
    word1 = FindC(H,word1)[0]
    word2 = FindC(H,word2)[0]
    #FInding Dot Product Of Words Embeddings
    dp = dotProductH(word1,word2)
    #Returning Magnitudes of Words
    mag1 = MagnitudeH(word1)
    mag2 = MagnitudeH(word2)
    denom = mag1 * mag2
    return dp/denom

#Returns the standard deviation in a Hash-Table
def standDevH(H):
    count = 0
    #Summing length of lists
    for i in H.item:
        count += len(i)
    avg = count/len(H.item)
    count = 0
    #Squaring Lengths
    for i in H.item:
        count += (len(i) - avg)*(len(i)-avg)
    avg = count/len(H.item)
    return math.sqrt(avg)

#Returns percent of empty lists
def perEmpty(H):
    count = 0
    for i in H.item:
        if len(i) == 0:
            count += 1
    return (count*100)/len(H.item)


#-------------------------------------------------------------------------------
#Functions that read the file and make them into nodes
#Converts the given file to an array of each line
def fileToArray(filename):
    file = open(filename, encoding="utf8")
    A = file.readlines()
    file.close
    return A

#Splits the elements of the string list into individuals
def arrSplit(A):
    B = []
    for i in range(len(A)):
        sp = A[i].split()
        B.append(sp)
    return B

#Creates a list with the string word element in one field (Word) and an float array in the second (Embedding)
def wrdEmb(A):
    B = []
    for i in range(len(A)):
        if A[i][0].isalpha():
            #Putting float elements in one list
            ls = np.array(A[i][1:])
            #Changing the elements from strings to float points
            lsr = ls.astype(np.float)
            lis = [A[i][0],lsr]
            B.append(lis)
    return B
#------------------------------------------------------------------------------

print()
print("What type of structure would you like?: ")
print("1. Binary Tree ")
print("2. Hash Table ")
txt = input("Choice: ")
txt = int(txt)

if txt == 1:
    words = fileToArray('Lab5 words.txt')
    words = arrSplit(words)
    
    print()
    print("Building Binary Search Tree...")
    print()
    
    start = time.time()
    T = None
    filename = 'glove.6B.50d.txt'
    inArr = fileToArray(filename)
    splitArr = arrSplit(inArr)
    wrdAndEm = wrdEmb(splitArr)
    #Sorting words from txt file
    wrdAndEm.sort()
    T = listToTree(T,wrdAndEm)
    end = time.time()
    
    #Stats of the BST
    print("BST Stats:")
    print("----------------------------------------------------------------------")
    print("Number of Nodes: ",numNodes(T))
    print("Height Of Binary Tree: ",getHeight(T))
    print("Time Taken To Build BST: ",end-start, " Seconds")
    print()
    print("Reading Word File To Determine Similarities...")
    print()
    print("Word Similarities Found:")
    
    start = time.time()
    #Printing Words and Displaying Similarities
    for i in range(len(words)):
        print(i+1,': ',words[i],end='')
        print(" = ",end='')
        print("{0:.4f}".format(compSim(T,words[i][0],words[i][1])))
    end = time.time()
    
    print()
    print("Time Taken To Find 60 Similarites: ",abs(start-end), " Seconds")



elif txt == 2:
    words = fileToArray('Lab5 words.txt')
    words = arrSplit(words)
    
    print()
    print("Creating Hash Table...")
    print()
    
    start = time.time()
    filename = 'glove.6B.50d.txt'
    inArr = fileToArray(filename)
    splitArr = arrSplit(inArr)
    wrdAndEm = wrdEmb(splitArr)
    hTable = crtHT(wrdAndEm)
    end = time.time()
    
    #Stats Of The Hash-Table
    print("Hash Table Stats: ")
    print("------------------------------------------------------------------")
    print("Intial Table Size: ", 11)
    print("Final Table Size: ", len(hTable.item))
    print("Load Factor: ",LoadFac(hTable))
    print("Percent of Empty Lists: ", perEmpty(hTable),'%')
    print("Standard Deviation of Length of Lists: ",standDevH(hTable))
    print("Time Taken To Build Hash Table: ",abs(start-end)," Seconds")
    print()
    print("Reading Word File To Determine Similarities...")
    print()
    print("Word Similarities Found:")
    
    start = time.time()
    #Displaying Words and Finding Similarities
    for i in range(len(words)):
        print(i+1,': ',words[i],end='')
        print(" = ",end='')
        print("{0:.4f}".format(compSimH(hTable,words[i][0],words[i][1])))
    end = time.time()
    
    print()
    print("Time Taken To Find 60 Similarites: ",abs(start-end), " Seconds")


else:
    print("Invalid Number")
