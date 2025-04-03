def resolver_torre_hanoi(n):
    # Inicializamos las torres como listas
    torre_origen = list(range(n, 0, -1))  # Torre inicial con los piedras
    torre_auxiliar = []  # Torre auxiliar vacía
    torre_destino = []  # Torre destino vacía

    # Método recursivo para resolver la Torre de Hanoi
    def mover_piedras(cantidad, origen, destino, auxiliar):
        if cantidad == 1:
            # Mover un piedra directamente
            piedra = origen.pop()
            destino.append(piedra)
            print(f"Mover piedra {piedra} de {origen} a {destino}")
        else:
            # Mover n-1 piedras a la torre auxiliar
            mover_piedras(cantidad - 1, origen, auxiliar, destino)
            # Mover el piedra restante a la torre destino
            mover_piedras(1, origen, destino, auxiliar)
            # Mover los n-1 piedras de la torre auxiliar a la torre destino
            mover_piedras(cantidad - 1, auxiliar, destino, origen)

    # Llamar al método recursivo
    mover_piedras(n, torre_origen, torre_destino, torre_auxiliar)

    # Mostrar el estado final de las torres
    print("Torre origen:", torre_origen)
    print("Torre auxiliar:", torre_auxiliar)
    print("Torre destino:", torre_destino)
    print("TOMA LO HAS CONSEGUIDO ESTE ES EL TESORO SECRETO:https://media.giphy.com/media/l0IynKSD9UkNZ88a4/giphy.gif?cid=790b7611i7wk5r666ep1ok6i17ivjueehqg8xkte2xcidymx&ep=v1_gifs_search&rid=giphy.gif&ct=g")


# Ejemplo de uso
resolver_torre_hanoi(3)