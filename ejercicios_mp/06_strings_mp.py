"""
Manejo de caracteres
"""

libro1= "Condorito"
print(f"Libro 1: {libro1}")
print(f"Tipo de datos: {type(libro1)}")

libro2= "Caquitas de colores"
print(f"Libro 2: {libro2}")
print(f"Tipo de datos: {type(libro2)}")

###### Funciones comunes de las variables String
print("Funciones comunes de texto")
autor_1 = "Harvey Specter"
autor_2 = "Mike Ross"

longitud_autor_1 = len(autor_1)
longitud_autor_2 = len(autor_2) 
print("libro droide 1: ", autor_1)
print("Longitud droide 1: ", longitud_autor_1)

print("libro droide 2: ", autor_2)
print("Longitud droide 2: ", longitud_autor_2)

print("Convertir Mayusculas y minisculas")
mesnaje = "Aprende a leer, no seas un lerdo"
mensaje_mayuscula = mesnaje.upper()
mensaje_minuscula = mesnaje.lower()
print("Mensaje en Mayuscula: ", mensaje_mayuscula)
print("Mensaje en minuscula: ", mensaje_minuscula)

print("Reemplazo de substring ")
mensaje = "Habia una vez...."
nuevo_mensaje = mensaje.replace("Blanca Nieves", "Mago de Oz")
print("Mensaje original: ",mensaje)
print("Nuevo mensaje: ", nuevo_mensaje)

print("Separación de cadenas en un arreglo")
libritos = "Naboo,Tatooine,Kmino"
print("Libritos: ", libritos)
lista_libritos = libritos.split(",")
print(lista_libritos)
print("Primer librito : ", lista_libritos[0])

print("Extraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:13]
verbo = mensaje[17:25]
print("adjetivo es : ", adjetivo)
print("verbo es : ", verbo)

print("Comprobaciones útiles")
codigo = "R2D2"
numero = "2026"
libro = "Univesidad UTE"
identificador = "DROIDE1"
print(codigo.isalnum())
print(numero.isdigit())
print(libro.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())