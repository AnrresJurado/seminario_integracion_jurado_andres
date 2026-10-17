print("Incluir Datos con Input")
nombre = input("¿Cuál es tu nombre?: ")
print(f"Hola, {nombre}!")
print("Bienvenido a la Biblioteca Central")
print("Hasta luego, " + nombre)

cantidad = int(input("¿Cuántos libros deseas llevar? "))
total = cantidad + 2
print("Libros totales: ", total)

print(" Conversiones ")
print("==== Kiosco de la Biblioteca ====")
nombre_cliente = input("Nombre del socio: ")
precio = float(input("Precio del libro: "))
cantidad = int(input("Cantidad: "))
total = cantidad * precio
print("Total a pagar: ", total)
print("Total a pagar (round): ", round(total, 2))
print(f"Total a pagar (f): ${total:.2f}")