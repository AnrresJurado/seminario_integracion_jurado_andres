print ("Inlcuir Datos con Input")
nombre = input("¿Cual es tu nombre?: ")
print(f"Hola, {nombre}, !")
print("Bienvenido a springfield")
print("Hasta Luego, "+nombre)

cantidad = int(input("¿Cuantas rosquillas hay? "))
total = cantidad +2
print("Rosquillas totales: ", total)

print(" Conversiones ")
print("====Tienda de APU====")
nombre_cliente = input("Nombre del cliente: ")
precio = float(input("Precio de rosquilla: "))
cantidad = int(input("Cantidad: "))
total = cantidad * precio
print("Total a pagra: ",total)
print("Total a pagar (round): ", round(total,2))
print(f"Total a pagara (f): ${total:.2f}")
