for pasillo_biblioteca in range(1, 11):
    if pasillo_biblioteca == 3: 
        print("Pasillo: ", pasillo_biblioteca, " - Fin del recorrido de la sección")
        continue
    elif pasillo_biblioteca == 7:
        print("Se encontró el libro buscado, la búsqueda finaliza") 
        break
    else:
        print("La exploración de estanterías continúa...")