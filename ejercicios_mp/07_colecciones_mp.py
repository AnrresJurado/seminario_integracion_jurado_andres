print("Estructuras de datos en Gestión de Biblioteca")

print("Listas (Colección ordenada y mutable)")
libros = ["Cien años de soledad", "El principito", "Rayuela"]
print("Libros: ", libros)
print("tipo: ", type(libros))

print("\nTuplas (Colección ordenada e inmutable)")
ubicacion_fisica = (3, 12, 4)  # Pasillo, Estante, Balda
print("Ubicación física: ", ubicacion_fisica)
print("tipo: ", type(ubicacion_fisica))

print("\nDiccionario (Pares clave-valor)")
ejemplar = {
    "codigo": "LIB-97884",
    "titulo": "Don Quijote de la Mancha",
    "disponible": True
}
print("Ejemplar: ", ejemplar)
print("tipo: ", type(ejemplar))

print("\nConjunto (Colección desordenada sin elementos duplicados)")
categorias = {
    "Novela",
    "Ciencia Ficción",
    "Historia"
}
print("Categorías: ", categorias)
print("tipo: ", type(categorias))