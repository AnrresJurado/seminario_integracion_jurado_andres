print("Condicional If")
print("Condicional Simple")
dinero = 10
if dinero >= 5:
    print("Homero puede comprar rosquillas")

print ("Programa Finalizo")


print ("Condicional IF-ELSE")
print ("CONDICIONAL DOS CAMINOS")
creditos = float(input("Cantidad de creditos disponibles: "))
precio_repuesto = float(input("Precio repuesto: "))

if (creditos >= precio_repuesto):
    print("Compar autorizada")
else: 
    print("Creditos insuficientes\n")
    print ("Busca solucion o turque")


print ("Condicional IF--ELIF--ELSE")
print ("CONDICIONAL CONDICONES MULTIPLES")
combustible = float(input("Combustible de la nave: "))

if (combustible >= 75):
    print("Optimo")
elif (combustible >=50): 
    print("Suficiente")
elif(combustible>=20):
     print ("Bajo")
else: 
    print("Critico")
    print("Localiza base mas cercana pliss")


print("Condicionales anidadas")
piloto = input("Nombre del piloto: ")
motor_funciona = input("El motor funciona (SI/NO): ")
combustible = int(input("Combustible disponible: "))

if (motor_funciona == "SI"):
    print("Motor Verificado")
    if combustible >= 50:
        print("Combustible suficiente")
        print("Participacion Autorizada")
    else: 
        print("Debe recrgara combustible")
else:
    print("No se puede participar")
    print("El motor necesita reparacion")