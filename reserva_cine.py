# Autor: Jesús Alberto Arias Mina
# Sala de cine 3x4 - Reserva de asientos

# 1. Crear matriz 3x4 con todos en 0 (libre)
asientos = [[0 for _ in range(4)] for _ in range(3)]

# 2. Pedir datos
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# 3. Reservar - poner 1
asientos[fila][columna] = 1

# 4. Mostrar sala completa
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
    