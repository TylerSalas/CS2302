#CS2302  
#Tyler Salas  
#Lab8
#Dr.Fuentes  
#Anindita Nath 
#Solves subset partition problem
import time

def subsetEqual(S,last):
    #Sums all the elements of S
    sumArray = sum(S)
  
    #Checks if the sum is odd if so partitioning is impossible
    if sumArray % 2 == 1:
        print("    No partition exists")
        return
    #Used to estimate the possible sum and to use as last element in pastCalc list
    posSum = sumArray//2
    #Stores calculations already made by program (coins diagram we did in class)
    pastCalc = [[False for i in range(posSum+1)] for i in range(last+1)]
    #Sets all zero points to false
    for i in range(1, posSum+1):
        pastCalc[0][i] = False
    #Sum of 0 is always True
    for i in range(last + 1):
        pastCalc[i][0] = True
        
    # Fills out the pastCalc table storing their true or false value (That sum is obtainable with set numbers)
    for i in range(1, last + 1):
        for j in range(1, posSum + 1):
            pastCalc[i][j] = pastCalc[i-1][j]
            if S[i - 1] <= j:
                pastCalc[i][j] = pastCalc[i][j] or pastCalc[i - 1][j - S[i - 1]]
                
    #If theres no s1=s2 no partition exists
    if pastCalc[last][posSum] == False:
        print("    No partition exists")
        return
    
    s1, s2 = [], []
    
    #While loop to determine elements of subset    
    while last>= 0 and posSum >=0:
        # if the current number in the subset doesnt contribute to reaching the possible sum and it is true it is put into s2
        if pastCalc[last - 1][posSum]:
            last -= 1
            s2.append(S[last])
        # else if it is true and not put into s2 it is put into s1
        elif pastCalc[last - 1][posSum - S[last - 1]]: 
            last -= 1
            posSum -= S[last]
            s1.append(S[last])
    return s1,s2

start = time.time()
S = [4,5,9,2,12,14,7,11,14,15,17] 
print("The subset S is:",S)
if subsetEqual(S,len(S)-1) is not None:
    print("The two partitions in S are:")
    print("    ",subsetEqual(S,len(S)-1))
end = time.time()
print(end-start)

S = [4,2,5,13,9] 
print("The subset S is:",S)
if subsetEqual(S,len(S)-1) is not None:
    print("The two partitions in S are:")
    print("    ",subsetEqual(S,len(S)-1))
    

