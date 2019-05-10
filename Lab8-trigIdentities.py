#CS2302  
#Tyler Salas  
#Lab8
#Dr.Fuentes  
#Anindita Nath 
#Detects trigometric identities

import matplotlib.pyplot as plt
import numpy as np
import random
import time
from math import *
import math

#Creates a list that holds identities and its count
def listMaker():
    identity = [[] for i in range(9)]

    a = "sin(t)"
    b = "cos(t)"
    c = "tan(t)"  
    d = "sec(t)"  #Secant = 1/cos(t)
    e = "-sin(t)"  
    f = "-cos(t)" 
    g = "-tan(t)"
    h = "sin(−t)" # -sin(t)
    i = "cos(−t)"  #cos(t)
    j = "tan(−t)"  #-tan(t)
    k = "sin(t)/cos(t)"  #tan(t)
    l = "(2*sin(t/2))*(cos(t/2))" #sin
    m = "sin(t)*sin(t)"
    n = "1 - (cos(t)*cos(t))" # sin^2
    o = "(1 - cos(2*t))/2" #Equal to sin^2
    p = "1/cos(t)"
    identity[0].append(a)
    identity[1].append(b)
    identity[2].append(c)
    identity[3].append(d)
    identity[4].append(e)
    identity[5].append(f)
    identity[6].append(g)
    identity[7].append(h)
    identity[8].append(m)
    for i in range(len(identity)):
        identity[i].append(0)
    return identity

#adds one to appropriate point in list holding identites
def addCount(identities,det):
    a = "sin(t)"
    b = "cos(t)"
    c = "tan(t)" 
    e = "-sin(t)"  
    f = "-cos(t)" 
    g = "-tan(t)"
    h = "sin(−t)" # -sin(t)
    m = "sin(t)*sin(t)"
    d = "1/cos(t)"
    if det == a:
        identities[0][1] += 1
    if det == b:
        identities[1][1] += 1
    if det == c:
        identities[2][1] += 1
    if det == d:
        identities[3][1] += 1
    if det == e:
        identities[4][1] += 1
    if det == f:
        identities[5][1] += 1
    if det == g:
        identities[6][1] += 1
    if det == h:
        identities[7][1] += 1
    if det == m:
        identities[8][1] += 1

#iterates through list to determine which identity had the highest number of matches
def detIden(identities):
    max = identities[0]
    for i in range(len(identities)):
        if identities[i][1] >= max[1]:
                max = identities[i]
        #print(max)
    return max
    

#Program that evaluates the trigometric identity of a function
def equal(f1,tries=1000,tolerance=0.0001):
    det = ""
    a = "sin(t)"
    b = "cos(t)"
    c = "tan(t)"  
    d = "sec(t)"  #Secant = 1/cos(t)
    e = "-sin(t)"  
    f = "-cos(t)" 
    g = "-tan(t)"
    h = "sin(−t)" # -sin(t)
    i = "cos(−t)"  #cos(t)
    j = "tan(−t)"  #-tan(t)
    k = "sin(t)/cos(t)"  #tan(t)
    l = "(2*sin(t/2))*(cos(t/2))" #sin
    m = "sin(t)*sin(t)"
    n = "1 - (cos(t)*cos(t))" # sin^2
    o = "(1 - cos(2*t))/2" #Equal to sin^2
    p = "1/cos(t)"
    identity = listMaker() 
    
    #For Loop to determine the trignometric identity according to above identities
    for i in range(tries):
        t = random.uniform(-math.pi,math.pi)
        y1 = eval(f1)
        
        y2 = eval(a)
        if np.abs(y2-y1) <= tolerance:
            det = a
            
        y2 = eval(b)
        if np.abs(y2-y1) <= tolerance:
            det = b
            
        y2 = eval(c)
        if np.abs(y2-y1) <= tolerance:
            det = c
            
        y2 = eval(p)
        if np.abs(y2-y1) <= tolerance:
            det = p
            
        y2 = eval(e)
        if np.abs(y2-y1) <= tolerance:
            det = e
            
        y2 = eval(f)
        if np.abs(y2-y1) <= tolerance:
            det = f
        
        y2 = eval(g)
        if np.abs(y2-y1) <= tolerance:
            det = g
            
        y2 = eval(e)
        if np.abs(y2-y1) <= tolerance:
            det = e
            
        y2 = eval(f)
        if np.abs(y2-y1) <= tolerance:
            det = f
            
        y2 = eval(g)
        if np.abs(y2-y1) <= tolerance:
            det = g
            
        y2 = eval(c)
        if np.abs(y2-y1) <= tolerance:
            det = c
        
        y2 = eval(a)
        if np.abs(y2-y1) <= tolerance:
            det = a
            
        y2 = eval(m)
        if np.abs(y2-y1) <= tolerance:
            det = m
            
        y2 = eval(n)
        if np.abs(y2-y1) <= tolerance:
            det = n
            
        y2 = eval(o)
        if np.abs(y2-y1) <= tolerance:
            det = m
            
        y2 = eval(p)
        if np.abs(y2-y1) <= tolerance:
            det = p
        addCount(identity,det)
        #print(det)
        #print(identity)
    return detIden(identity)[0]

t = 5
a = "sin(t)"
b = "cos(t)"
c = "tan(t)"  
d = "sec(t)"  #Secant = 1/cos(t)
e = "-sin(t)"  
f = "-cos(t)" 
g = "-tan(t)"
h = "sin(−t)" # -sin(t)
i = "cos(−t)"  #cos(t)
j = "tan(−t)"  #-tan(t)
k = "sin(t)/cos(t)"  #tan(t)
l = "(2*sin(t/2))*(cos(t/2))" #sin
m = "sin(t)*sin(t)"
n = "1 - (cos(t)*cos(t))" # sin^2
o = "(1 - cos(2*t))/2" #Equal to sin^2
p = "1/cos(t)"


start = time.time()
print("Equation:",a)
print("Program's Determined Trigonometric Identity: ",equal(a))
print()
print("Equation:",b)
print("Program's Determined Trigonometric Identity: ",equal(b))
print()
print("Equation:",c)
print("Program's Determined Trigonometric Identity: ",equal(c))
print()
print("Equation:",e)
print("Program's Determined Trigonometric Identity: ",equal(e))
print()
print("Equation:",f)
print("Program's Determined Trigonometric Identity: ",equal(f))
print()
print("Equation:",g)
print("Program's Determined Trigonometric Identity: ",equal(g))
print()
print("Equation:",k)
print("Program's Determined Trigonometric Identity: ",equal(k))
print()
print("Equation:",l)
print("Program's Determined Trigonometric Identity: ",equal(l))
print()
print("Equation:",m)
print("Program's Determined Trigonometric Identity: ",equal(m))
print()
print("Equation:",n)
print("Program's Determined Trigonometric Identity: ",equal(n))
print()
print("Equation:",o)
print("Program's Determined Trigonometric Identity: ",equal(o))
print()
print("Equation:",p)
print("Program's Determined Trigonometric Identity: ",equal(p))
print()
end = time.time()
print(end-start)
