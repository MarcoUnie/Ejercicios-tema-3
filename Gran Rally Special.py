# Lista de naves espaciales (nombre, longitud, tripulantes, pasajeros)
naves = [
    {"nombre": "Cometa Veloz", "longitud": 120, "tripulantes": 10, "pasajeros": 50},
    {"nombre": "Titán del Cosmos", "longitud": 200, "tripulantes": 15, "pasajeros": 100},
    {"nombre": "GX-1 Explorer", "longitud": 150, "tripulantes": 8, "pasajeros": 6},
    {"nombre": "GX-2 Voyager", "longitud": 180, "tripulantes": 12, "pasajeros": 20},
    {"nombre": "Estrella Fugaz", "longitud": 90, "tripulantes": 5, "pasajeros": 10},
    {"nombre": "Nebulosa Andrómeda", "longitud": 250, "tripulantes": 20, "pasajeros": 200},
    {"nombre": "Aurora Boreal", "longitud": 110, "tripulantes": 7, "pasajeros": 8},
]

# Ordenar la lista de naves por nombre ascendente y longitud descendente
naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))

# Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
info_cometa_veloz = next((nave for nave in naves if nave["nombre"] == "Cometa Veloz"), None)
info_titan_cosmos = next((nave for nave in naves if nave["nombre"] == "Titán del Cosmos"), None)

# Determinar las cinco naves con mayor cantidad de pasajeros
top_5_pasajeros = sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:5]

# Determinar la nave que requiere la mayor cantidad de tripulación
nave_mayor_tripulacion = max(naves, key=lambda x: x["tripulantes"])

# Mostrar todas las naves cuyo nombre comience con "GX"
naves_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]

# Listar todas las naves que pueden llevar seis o más pasajeros
naves_seis_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]

# Mostrar información de la nave más pequeña y la más grande
nave_mas_pequena = min(naves, key=lambda x: x["longitud"])
nave_mas_grande = max(naves, key=lambda x: x["longitud"])

# Resultados
print("Naves ordenadas por nombre ascendente y longitud descendente:")
for nave in naves_ordenadas:
    print(nave)

print("\nInformación de 'Cometa Veloz':", info_cometa_veloz)
print("Información de 'Titán del Cosmos':", info_titan_cosmos)

print("\nCinco naves con mayor cantidad de pasajeros:")
for nave in top_5_pasajeros:
    print(nave)

print("\nNave que requiere mayor cantidad de tripulación:", nave_mayor_tripulacion)

print("\nNaves cuyo nombre comienza con 'GX':")
for nave in naves_gx:
    print(nave)

print("\nNaves que pueden llevar seis o más pasajeros:")
for nave in naves_seis_pasajeros:
    print(nave)

print("\nNave más pequeña:", nave_mas_pequena)
print("Nave más grande:", nave_mas_grande)