import numpy as np

# Probabilidades + Valores
outcomes = np.array([1, -5, 5, -100])
probs = np.array([0.70, 0.10, 0.15, 0.05])

def session_until_goal_or_bust(initial_stack=100, target_stack=200, opponent_stack=100):
    stack_p1 = initial_stack
    stack_p2 = opponent_stack
    historial_p1 = [stack_p1]
    historial_p2 = [stack_p2]
    
    gains_p1 = []  
    gains_p2 = []

    wins_p1 = 0
    wins_p2 = 0
    hands_played = 0

    while 0 < stack_p1 < target_stack:
        change = np.random.choice(outcomes, p=probs)
        
        # Ajuste de all-in
        if change > 0:
            actual_gain = min(change, stack_p2)  
            stack_p1 += actual_gain
            stack_p2 -= actual_gain
            wins_p1 += 1
        else:
            actual_loss = max(change, -stack_p1)  
            stack_p1 += actual_loss
            stack_p2 -= actual_loss
            wins_p2 += 1
        
        gains_p1.append(stack_p1 - historial_p1[-1])
        gains_p2.append(stack_p2 - historial_p2[-1])
        
        historial_p1.append(stack_p1)
        historial_p2.append(stack_p2)
        hands_played += 1

    gains_p1 = np.array(gains_p1)
    gains_p2 = np.array(gains_p2)

    print(f"Partidas jugadas: {hands_played}")
    print("\nPlayer 1:")
    print("Ganancias totales:", stack_p1 - initial_stack)
    print("Valor esperado aproximado de la ganancia por mano:", np.mean(gains_p1))
    print("Varianza aproximada de la ganancia por mano:", np.var(gains_p1))
    print("Historial de stacks:", historial_p1)
    
    print("\nPlayer 2:")
    print("Ganancias totales:", stack_p2 - opponent_stack)
    print("Valor esperado aproximado de la ganancia por mano:", np.mean(gains_p2))
    print("Varianza aproximada de la ganancia por mano:", np.var(gains_p2))
    print("Historial de stacks:", historial_p2)

# Ejecutar la sesión
session_until_goal_or_bust()
