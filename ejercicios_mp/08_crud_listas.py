libros = [
    {"id": 2, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "estado": "Disponible"},
    {"id": 3, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "estado": "Disponible"}
]
id_publico = 4

def create():
    global id_publico
    print("Registrar libro")
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    estado = input("Estado (Disponible, Prestado, Reservado): ")
    nuevo_libro = {
        "id": id_publico,
        "titulo": titulo,
        "autor": autor,
        "estado": estado
    }
    libros.append(nuevo_libro)
    id_publico += 1
    print("Libro registrado exitosamente")

def read():
    print("Lista de libros en la biblioteca:")
    for libro in libros:
        print(f"ID: {libro['id']} | Título: {libro['titulo']} | Autor: {libro['autor']} | Estado: {libro['estado']}")

def update():
    print("Actualizar información del libro")
    try:
        id_update = int(input("Ingrese el ID del libro a modificar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
        
    encontrado = False
    for libro in libros:
        if libro["id"] == id_update:
            libro["titulo"] = input("Nuevo título: ")
            libro["autor"] = input("Nuevo autor: ")
            libro["estado"] = input("Nuevo estado: ")
            print("Libro actualizado correctamente")
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado.")

def delete():
    print("Eliminar libro del inventario")
    try:
        id_delete = int(input("Ingrese el ID del libro a borrar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
        
    encontrado = False
    for libro in libros:
        if libro["id"] == id_delete:  
            libros.remove(libro)
            print("Libro eliminado del sistema")
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado.")

def menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA ---")
        print("1. Registrar libro")
        print("2. Ver catálogo")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Seleccione una opción del 1 al 5: ")
        
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Cerrando sistema de biblioteca...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()