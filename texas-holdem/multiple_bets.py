import numpy as np

# Possible results and probabilities
outcomes = np.array([1, -5, 5, -100])   
probs = np.array([0.70, 0.10, 0.15, 0.05])

def session(hands=100, player_1=100, player_2=100):
    stack_p1 = player_1
    stack_p2 = player_2
    historial_p1 = [stack_p1]
    historial_p2 = [stack_p2]

    wins_p1 = 0
    wins_p2 = 0
    
    for _ in range(hands):
        change = np.random.choice(outcomes, p=probs)
        if (change > 0): 
            if change == outcomes[-1]: 
                change = min(stack_p1, stack_p2)
            stack_p1 += change
            stack_p2 -= change 
            wins_p1 += 1
        else: 
            stack_p1 += change
            stack_p2 -= change
            wins_p2 += 1
        historial_p1.append(stack_p1)
        historial_p2.append(stack_p2)
        outcomes[-1] = stack_p1
        
        if stack_p1 <= 0 or stack_p2 <= 0:  
            break
    
    print ("\nPlayer 1:","\nPartidas ganadas:", wins_p1, "\nHistorial:", np.array(historial_p1), "\n", "\nPlayer 2:", "\nPartidas ganadas:", wins_p2, np.array(historial_p2), )

result = session()