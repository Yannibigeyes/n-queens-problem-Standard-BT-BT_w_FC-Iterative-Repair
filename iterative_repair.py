'''
Authors:    Yongyang Liu <liuyongyang@gatech.edu>
            
Date:       9 Sept 2020
'''


import time
import numpy as np
import matplotlib.pyplot as plt

# ## Iterative Repair (Min-Conflict Heuristic)  (iterative repair) 


import random
##### With reference to https://gist.github.com/vedantk/747203  #####
def Num_conflictions(V, n, V_idx, value):
    num_confct = 0
    for i in range(n):                            # Col: Variables index
        if i == V_idx:                            # Pass itself
            continue
        if V[i] == value or abs(V[i] - value) == abs(i - V_idx):
            num_confct += 1                       # Line and diagonal constraint
    return num_confct

def Iterative_repair(V, n, start_time):
    elapsed_time = time.time()-start_time         # Time checking
    while elapsed_time < 600:
        # Obtain a list of number_conflict over variable
        Conflicts_num = [Num_conflictions(V, n, V_idx, V[V_idx]) for V_idx in range(n)] 
        
        if sum(Conflicts_num) == 0:               # Consistent result
            for i in range(n):
                V[i]+=1
            return V
        
        # Random varibale ordering: randomly select a variable which has conflict
        Conflicts_V_idx = random.choice([i for i in range(n) if Conflicts_num[i] > 0])
        
        # Obtain a list of number_conflict over whole Domain for this variable
        Conflicts_V_values = [Num_conflictions(V, n, Conflicts_V_idx, row) for row in range(n)]
        
        # Random value ordering: randomly select a value which has minimum number_conflict
        V[Conflicts_V_idx] = random.choice([i for i in range(n) if Conflicts_V_values[i] == min(Conflicts_V_values)])   
        
        #V[Conflicts_V] = Conflicts_V_values.index(min(Conflicts_V_values))  # fixed value ordering
        
        elapsed_time = time.time()-start_time     # Time checking
        
    return 'Time_out' 

Run_Tim_MCH = []
n = 4
Loop = True
while Loop == True:
    start_time = time.time()
    
    # Initialize Variable assignments with random value
    V = [random.choice([i for i in range(n)]) for j in range(n)]  
    result = Iterative_repair(V, n, start_time)
    elapsed_time = time.time()-start_time
    Run_Tim_MCH.append(elapsed_time)
    #print('Result of %d Queues: '% (n), *result, sep = ", ") 
    print('Time of %d Queues (s): %1.12f' % (n, elapsed_time))
    
    n+=1
    if result == 'Time_out':
        Loop = False
