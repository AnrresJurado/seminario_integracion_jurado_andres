print("OPERADORES")
print("Operadores Aritmeticos")
print("+ Suma: ", 10, "+", 5, "=", 10+5)
print("- Resta: ", 10, "-", 5, "=", 10-5)
print("* Multiplicacion: ", 10, "*", 5, "=", 10*5)
print("/ Division: ", 10, "/", 3, "=", 10/3)
print("// Division entera: ", 10, "//", 3, "=", 10//3)
print("% Residuo: ", 10, "%", 3, "=", 10%3)
print("** Potencia: ", 2, "**", 3, "=", 2**3)

print("Tabla de multiplicar del 7")
print(7, "*", 1, "=", 7*1)
print(7, "*", 2, "=", 7*2)
print(7, "*", 3, "=", 7*3)
print(7, "*", 4, "=", 7*4)
print(7, "*", 5, "=", 7*5)
print(7, "*", 6, "=", 7*6)
print(7, "*", 7, "=", 7*7)
print(7, "*", 8, "=", 7*8)
print(7, "*", 9, "=", 7*9)
print(7, "*", 10, "=", 7*10)

print("Operadores de Comparacion")
print("== Igual a : ", 10, "==", 10, 10==10)
print("== Igual a : ", 10, "==", 5, 10==5)
print("!= Desigual a : ", 10, "!=", 10, 10!=10)
print("!= Desigual a : ", 10, "!=", 5, 10!=5)
print("> Mayor que: ", 15, ">", 10, 15>10)
print("> Mayor que: ", 15, ">", 20, 15>20)
print("< Menor que: ", 10, "<", 15, 10<15)
print("< Menor que: ", 20, "<", 15, 20<15) 
print(">= Mayor o igual que: ", 15, ">=", 10, 15>=10) 
print(">= Mayor o igual que: ", 10, ">=", 10, 10>=10) 
print("<= Menor o igual que: ", 10, "<=", 15, 10<=15) 
print("<= Menor o igual que: ", 15, "<=", 10, 15<=10) 

print("OPERADORES LOGICOS")
print("Operadores and : (10==10)and(5>3)", (10==10)and(5>3))
print("Operadores and : (10==10)and(5>8)", (10==10)and(5>8))
print("Operadores or : (10==10)or(5>3)", (10==10)or(5>3))
print("Operadores or : (10==12)or(5>3)", (10==12)or(5>3))
print("Operadores not : not(10==12)", not(10==12))
print("Operadores not : not(10==10)", not(10==10))

tiene_membresia = True
biblioteca_abierta = True 

puede_prestar = tiene_membresia and biblioteca_abierta
print("¿Puede prestar libro? ", puede_prestar)

es_socio_vip = True
tiene_multa_pendiente = False 
acceso_prestamo_especial = es_socio_vip or tiene_multa_pendiente
print("¿Préstamo especial aprobado? ", acceso_prestamo_especial)