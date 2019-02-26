#CS2302  
#Tyler Salas  
#Lab1-No.4
#Dr.Fuentes  
#Anindita Nath 
#Sort lists with different methods and count numbers of comparison
import random
import time
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head = L.head.next
        L.head = Node(x)

def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
      
def getLength(L):
    count = 0
    if IsEmpty(L):
        return 0
    else:
        temp = L.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

def copy(L):
    t = List()
    temp = L.head
    while temp is not None:
        Append(t, temp.item)
        temp = temp.next
    return t

def createList(n):
    L = List()
    for i in range(n):
        Append(L,random.randint(0,101))
    return L   

def copyLeft(L, mid):
    t = List()
    temp = L.head
    for i in range(mid):
        Append(t, temp.item)
        temp = temp.next
    return t

def copyRight(L, mid):
    t = List()
    temp = L.head
    for i in range(mid):
        temp = temp.next
    while temp is not None:
        Append(t, temp.item)
        temp = temp.next
    return t
 
def bubbleSort(L):
    global count
    change = True
    while change:
        t = L.head
        change = False
        while t.next is not None:   
            if t.item > t.next.item:
                count += 1
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change = True
            t = t.next

def getMedian(L):
    t = L.head
    mid = getLength(L)//2
    for i in range(mid):
        t = t.next
    return t.item

def concatenate(L1, L2):
    if IsEmpty(L1):
        if IsEmpty(L2):
            return
        else:
            L1.head = L2.head
            L1.tail = L2.tail
            return
    if IsEmpty(L2):
        return
    else:
        L1.tail.next = L2.head
        L1.tail = L2.tail
    return

def mergeSort(L):
    global count
    temp = L.head
    if getLength(L) >= 2:
        mid = getLength(L)//2
        lefthalf = copyLeft(L,mid)
        righthalf = copyRight(L,mid)
        mergeSort(lefthalf)
        mergeSort(righthalf)
        ltemp = lefthalf.head
        rtemp = righthalf.head
        
        while ltemp is not None and rtemp is not None:
            count += 1
            if ltemp.item < rtemp.item:
                temp.item = ltemp.item
                ltemp = ltemp.next
            else:
                temp.item = rtemp.item
                rtemp = rtemp.next
            temp = temp.next
        while ltemp is not None:
            temp.item = ltemp.item
            ltemp = ltemp.next
            temp = temp.next
        while rtemp is not None:
            temp.item = rtemp.item
            rtemp = rtemp.next
            temp = temp.next
         
def getItem(L,x):
    temp = L.head
    i = 0
    while i < x and temp.next is not None:
        temp = temp.next
        i += 1
    return temp

def quickSort(L):
   quickSorter(L,0,getLength(L)-1)

def quickSorter(L,first,last):
   if first<last:
       
       
       splitpoint = partition(L,first,last)
       
       quickSorter(L,first,splitpoint-1)
       quickSorter(L,splitpoint+1,last)
def partition(L,first,last):
    global count
    temp = getItem(L,first)
    pivot = temp
    
    leftmark = first+1
    rightmark = last
    fst = getItem(L,leftmark)
    right = getItem(L,last)
    done = False
    while not done:
        if right.item < fst.item:
                t = fst.item
                fst.item = right.item
                right.item = t 
        while leftmark <= rightmark and fst is not None and fst.item <= pivot.item:
            count += 1
            leftmark = leftmark + 1
            fst = fst.next
        while right.item > pivot.item and rightmark >= leftmark:
            count += 1
            rightmark = rightmark -1
            right = getItem(L,rightmark)
        if rightmark <= leftmark:
            done = True
        else:
            t = fst.item
            fst.item = right.item
            right.item = t
    t = pivot.item
    pivot.item = right.item
    right.item = t
    return rightmark
def quickSort2(L):
   quickSorter2(L,0,getLength(L)-1)

def quickSorter2(L,first,last):
    if first>=last:
        return
    else:
        splitpoint = partition(L,first,last)
        det = detMedian(L)
        if det:
            quickSorter2b(L,first,splitpoint-1)
        else:
            quickSorter2b(L,splitpoint+1,last)    

def quickSorter2b(L,first,last):
    if first >= last:
        return
    else:
        splitpoint = partition(L,first,last)
        quickSorter(L,first,splitpoint-1)
        quickSorter(L,splitpoint+1,last)
       
def detMedian(L):
    median = getItem(L,getLength(L)//2)
    temp = L.head
    tall = 0
    short = 0
    while temp is not None:
        if median.item > temp.item:
            short += 1
        else:
            tall += 1
        temp = temp.next
    if short <= tall:
        return True
    else:
        return False
     
def bMedian(L):
    C = copy(L)
    bubbleSort(C)
    return getItem(C,getLength(C)//2)
def mMedian(L):
    C = copy(L)
    mergeSort(C)
    return getItem(C,getLength(C)//2)
def qMedian(L):
    C = copy(L)
    quickSort(C)
    return getItem(C,getLength(C)//2)
def q2Median(L):
    C = copy(L)
    quickSort2(C)
    return getItem(C,getLength(C)//2)
#Initializing lists to be used all lists are made the same for accurate results

L1 = createList(15)
L2 = copy(L1)
L3 = copy(L1)
L4 = copy(L1)

count = 0
b = bMedian(L1)
count = 0
m = mMedian(L2)
count = 0
q = qMedian(L3)
count = 0
q2 = q2Median(L4)
#Bubble Sorting and print original/new/comparisons of List
start = time.time()
print("Bubble Sort:")
count = 0
print("Original List: ")
Print(L1)
bubbleSort(L1)
print("Sorted List:")
Print(L1)
print("Median:",b.item)
print("Number of Comparisons: ",count)
end = time.time()
print(end - start)
print()

#Merge Sorting and print original/new/comparisons of List
start = time.time()
print("Merge Sort")
print("Original List: ")
count = 0
Print(L2)
mergeSort(L2)
print("Sorted List:")
Print(L2)
print("Median:",m.item)
print("Number of Comparisons: ",count)
end = time.time()
print(end - start)
print()

#Quick Sorting and print original/new/comparisons of List
start = time.time()
print("Quick Sort")
print("Original List: ")
count = 0
Print(L3)
quickSort(L3)
print("Sorted List:")
Print(L3)
print("Median:",q.item)
print("Number of Comparisons: ",count)
end = time.time()
print(end - start)
print()

#Quick Sorting and print original/new/comparisons of List
start = time.time()
print("Quick Sort Modified")
print("Original List: ")
count = 0
Print(L4)
quickSort2(L4)
print("Sorted List:")
Print(L4)
print("Median:",q2.item)
print("Number of Comparisons: ",count)
end = time.time()
print(end - start)
print()






