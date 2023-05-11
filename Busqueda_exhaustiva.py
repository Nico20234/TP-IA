# Definir los límites del espacio de búsqueda
x_min = -10
x_max = 10

# Definir el incremento de avance
delta_h = 0.1

# Definir la posición inicial
current_position = (0, 0)

# Definir la posición objetivo
target_position = (5, 0)

# Definir una variable para almacenar la mejor solución encontrada
best_solution = None

# Realizar la búsqueda exhaustiva
for x in range(int((x_min - current_position[0]) / delta_h), int((x_max - current_position[0]) / delta_h)):
    # Moverse a la nueva posición
    new_position = (current_position[0] + x * delta_h, current_position[1])
    
    # Calcular la distancia a la posición objetivo
    distance = ((new_position[0] - target_position[0]) ** 2 + (new_position[1] - target_position[1]) ** 2) ** 0.5
    
    # Comprobar si es la mejor solución encontrada hasta ahora
    if best_solution is None or distance < best_solution[0]:
        best_solution = (distance, new_position)
    
# Imprimir la mejor solución encontrada
print("La mejor solución encontrada es la posición", best_solution[1], "con una distancia de", best_solution[0])
