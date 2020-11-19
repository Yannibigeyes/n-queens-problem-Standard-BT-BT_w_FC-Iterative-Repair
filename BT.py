'''
Authors:    Yongyang Liu <liuyongyang@gatech.edu>
            
Date:       9 Sept 2020
'''


import time
import numpy as np
import matplotlib.pyplot as plt

# ## Backtrack Search (BT) 


def Constraint(a_temp,i):
    if i == 1:
        return 'consistent'                       # for in case that the first variable
    
    for j in range(i-1):                          # Line and diagonal constraint
        if V[j] != a_temp and abs(V[j] - a_temp)!= abs(j+1 - i):
            continue
        else:
            return 'inconsistent' 
    return 'consistent'
    

def Select_Value(i, D_temp):
    while D_temp[i-1, 0] != 0:                    # D_temp is not empty
        a_temp = D_temp[i-1,0]                    # select the first item from D_temp
        
        D_temp[i-1, 0:n-1] = D_temp[i-1,1:]       # Remove the first item from D_temp
        D_temp[i-1, n-1] = 0                      # Remove the first item from D_temp
        
        if i == 1:                                # First variable
            return a_temp                        

        if Constraint(a_temp, i)=='consistent':
            return a_temp                         # Consistent value
    

    return None                                   # D_temp is empty and no consistent value

def Backtrack(start_time):
    i = 1                                         # Initiate variable 
    D_temp[i-1] = D[i-1].copy()                   # copy domain for i
    
    while i>=1 and i <= n:
        
        elapsed_time = time.time()-start_time     # Time checking
        if elapsed_time > 600:
            return 'Time_out' 
        
        V[i-1] = Select_Value(i, D_temp)          # Instantiate variable
        if V[i-1] == None:
            i = i-1
        else:
            i = i+1
            if i>=1 and i <= n:
                D_temp[i-1] = D[i-1].copy()       # Reset Domain copy
    
    if i == 0:
        return 'Inconsistent'
    else:
        return V


Run_Tim_BT = []

n = 4
Loop = True
while Loop == True:
    start_time = time.time()
    D = np.zeros([n,n],dtype=np.int64)            # col, row
    D_temp = D.copy()
    #V = np.zeros([n,1],dtype=np.int64)           # col
    V = [0] * n
    for i in range(n):
        for j in range(n):
            D[i,j] = j+1
    
    result = Backtrack(start_time)
    
    elapsed_time = time.time()-start_time
    Run_Tim_BT.append(elapsed_time)
    #print('Result of %d Queues: '% (n), *result, sep = ", ") 
    print('Time of %d Queues (s): %1.12f' % (n, elapsed_time))
    
    n+=1
    if result == 'Time_out':
        Loop = False

    
