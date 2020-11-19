'''
Authors:    Yongyang Liu <liuyongyang@gatech.edu>
            
Date:       9 Sept 2020
'''


import time
import numpy as np
import matplotlib.pyplot as plt

# ## Standard Search 



def Constraint(V):
    for j in range(n):                            # Col: Variables index
        for i in range(n):                        # Col: Variables index
            if i == j:                            # Pass itself
                continue
            if V[i] == V[j]  or abs(V[i] - V[j] ) == abs(i - j): # Line and diagonal constraint
                return 'inconsistent'                       
    return 'consistent'


def Standard(start_time):
    D_temp = D.copy()
    #print(D_temp)
    while D_temp[0,0]!= 0:                          # Whole domains are not empty  
        
        elapsed_time = time.time()-start_time       # Time checking
        if elapsed_time > 600:
            return 'Time_out'

        # If a certain domain is empty caused by value remove in last step 
        for j in range(n-1, -1, -1):                # n-1, n-2, n-3, ..., 0
            if D_temp[j, 0] == 0:                   # Domain of j is empty
                D_temp[j-1, 0:n-1] = D_temp[j-1,1:] # remove value from variable previous domain
                D_temp[j-1, n-1] = 0   
                D_temp[j] = D[j].copy()             # Reset itself
        
        #print(D_temp)
        V = D_temp[:, 0]                            # Assignment
        #print(V)
        
        V_idx = n-1                                 # the last variable n
        if Constraint(V)=='consistent':
            return V                                # Consistent result
        else:
            while D_temp[V_idx,0]==0:               # if current Variable domain is empty
                V_idx -= 1                          # come to the previous variable
            
            D_temp[V_idx, 0:n-1] = D_temp[V_idx,1:] # remove value from variable V_idx domain
            D_temp[V_idx, n-1] = 0  
            
            if V_idx >=0 and V_idx < n-1:         
                D_temp[V_idx+1:n] = D[V_idx+1:n].copy() # Reset domain copies for all V_idx > i
            #print(D_temp)          
    return 'Inconsistent'
    

Run_Tim_Standard = []

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
    
    result = Standard(start_time)
    
    elapsed_time = time.time()-start_time
    Run_Tim_Standard.append(elapsed_time)
    #print('Result of %d Queues: '% (n), *result, sep = ", ") 
    print('Time of %d Queues (s): %1.12f' % (n, elapsed_time))
    
    n+=1
    if result == 'Time_out':
        Loop = False

