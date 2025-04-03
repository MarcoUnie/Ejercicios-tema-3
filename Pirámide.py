def resolver_torre_hanoi(n):
    # Inicializamos las torres como listas
    torre_origen = list(range(n, 0, -1))  # Torre inicial con los discos
    torre_auxiliar = []  # Torre auxiliar vacía
    torre_destino = []  # Torre destino vacía

    # Método recursivo para resolver la Torre de Hanoi
    def mover_discos(cantidad, origen, destino, auxiliar):
        if cantidad == 1:
            # Mover un disco directamente
            disco = origen.pop()
            destino.append(disco)
            print(f"Mover disco {disco} de {origen} a {destino}")
        else:
            # Mover n-1 discos a la torre auxiliar
            mover_discos(cantidad - 1, origen, auxiliar, destino)
            # Mover el disco restante a la torre destino
            mover_discos(1, origen, destino, auxiliar)
            # Mover los n-1 discos de la torre auxiliar a la torre destino
            mover_discos(cantidad - 1, auxiliar, destino, origen)

    # Llamar al método recursivo
    mover_discos(n, torre_origen, torre_destino, torre_auxiliar)

    # Mostrar el estado final de las torres
    print("Torre origen:", torre_origen)
    print("Torre auxiliar:", torre_auxiliar)
    print("Torre destino:", torre_destino)

# Ejemplo de uso
resolver_torre_hanoi(74)