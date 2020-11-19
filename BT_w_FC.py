'''
Authors:    Yongyang Liu <liuyongyang@gatech.edu>
            
Date:       9 Sept 2020
'''


import time
import numpy as np
import matplotlib.pyplot as plt

# ## Backtrack with Forward checking Search (BT_w_FC) 


def Constraint_FC(a_temp, b_temp, i, k):
    
    if a_temp == b_temp or abs(a_temp - b_temp)== abs(i - k):
        return 'inconsistent'
    
    if i!= 1:                                     # Line and diagonal constraint
        for j in range(i-1):                      # Consistency between a and vector a_i-1 + b and vector a_i-1
            if V[j] != a_temp and abs(V[j] - a_temp)!= abs(j+1 - i) and V[j] != b_temp and abs(V[j] - b_temp)!= abs(j+1 - k):
                continue
            else:
                return 'inconsistent'
    
    return 'consistent'
    

def Select_Value_FC(i, D_temp):
    while D_temp[i-1, 0] != 0:                    # D_temp is not empty
        a_temp = D_temp[i-1,0]                    # Select the first item from D_temp
        
        D_temp[i-1, 0:n-1] = D_temp[i-1,1:]       # Remove the first item from D_temp
        D_temp[i-1, n-1] = 0                      # Remove the first item from D_temp
        
        
        empty_k = False
        #print(D_temp)
        for k in range(i,n):                      # For all k > i 
            #print('k= %d' %(k))
            #print(D_temp[k])
            for j in range(n):
                b_temp = D_temp[k,j]
                #print(b_temp)
                if b_temp==0:
                    break
                
                if Constraint_FC(a_temp, b_temp, i, k+1)=='inconsistent':
                    D_temp[k,j] = 0
            
            if D_temp[k].sum()== 0:               # Domain[k] is empty
                D_temp[i:n] = D[i:n].copy()       # Reset domain copies for all k > i
                empty_k = True
                #print('empty')
                break
            
            #print(D_temp[k])
            
            idx_temp =D_temp[k].nonzero()         # Sort
            nonzeros_tem = D_temp[k,idx_temp]
            D_temp[k] = np.zeros([1,n])
            D_temp[k,0:len(idx_temp[0])] = nonzeros_tem
            
            #print(D_temp[k])
            
        if empty_k==False:                        # If no neighbor k is empty, then a is consistent value, otherwise choose a new a
            #print('no empty')
            #print(D_temp)
            return a_temp
    
    return None                                   # D_temp is empty and no consistent value

def Backtrack_Forward_Checking(start_time):
    i = 1                                         # Initiate variable 
    D_temp = D.copy()                             # copy all domains
    
    #print(D_temp)
    while i>=1 and i <= n:
        
        elapsed_time = time.time()-start_time     # Time checking
        if elapsed_time > 600:
            return 'Time_out' 
        
        V[i-1] = Select_Value_FC(i, D_temp)       # Instantiate variable
        #print(V)
        if V[i-1] == None:
            if i>=1 and i < n:
                D_temp[i-1:n] = D[i-1:n].copy()       # Reset domain copies for all k >= i
            i = i-1  
            #print('i= %d' %(i))
        else:
            i = i+1
            #print('i= %d' %(i))
            
    
    if i == 0:
        return 'Inconsistent'
    else:
        return V


Run_Tim_BT_FC = []

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
    
    result = Backtrack_Forward_Checking(start_time)
    elapsed_time = time.time()-start_time
    Run_Tim_BT_FC.append(elapsed_time)
    #print('Result of %d Queues: '% (n), *result, sep = ", ") 
    print('Time of %d Queues (s): %1.12f' % (n, elapsed_time))
    
    n+=1
    if result == 'Time_out':
        Loop = False





