import numpy as np

# Possible results and probabilities
outcomes = np.array([1, -5, 5, -100])   
probs = np.array([0.70, 0.10, 0.15, 0.05])

def session(hands=100, player_1=100, player_2=100):
    stack_p1 = player_1
    stack_p2 = player_2
    historial_p1 = [stack_p1]
    historial_p2 = [stack_p2]
    
    for _ in range(hands):
        change = np.random.choice(outcomes, p=probs)
        print(change)
        if (change > 0): 
            stack_p1 += change
            stack_p2 -= change
            historial_p1.append(stack_p1)
            historial_p2.append(stack_p2)
            outcomes[-1] = stack_p1
        else: 
            stack_p1 -= change
            stack_p2 += change
            historial_p1.append(stack_p1)
            historial_p2.append(stack_p2)
            outcomes[-1] = stack_p1
        
        if stack_p1 <= 0 or stack_p2 <= 0:  
            break
    
    print ("\nPLayer 1: \n", np.array(historial_p1), "\nPlayer 2: \n", np.array(historial_p2))

# 1 Session
result = session()