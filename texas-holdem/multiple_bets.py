import numpy as np
import matplotlib.pyplot as plt

# Probabilidades y ganancias/pérdidas
outcomes = np.array([1, -5, 5, -100])   # ganancias por mano
probs = np.array([0.70, 0.10, 0.15, 0.05])

def session(manos=100, stack_inicial=100):
    stack = stack_inicial
    historial = [stack]
    
    for _ in range(manos):
        cambio = np.random.choice(outcomes, p=probs)
        stack += cambio
        historial.append(stack)
        
        if stack <= 0: 
            break
    
    print(np.array(historial))

# Simulación de varias sesiones
reuslt = session()
