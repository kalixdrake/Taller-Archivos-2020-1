def elegir_localidad(lista,localidades):
    """Se usa para una vez elegida la estadistica deseada, colocar la localidad de la cual se quiere saber"""
    try:
        localidad_deseada = int(input("Ingrese el número de la localidad"))
    except ValueError:
        print("Debe ingresar un numero entero, por favor intentelo de nuevo \n")
    if lista[localidad_deseada] == "Todas":
        for i in localidades:
            print(i,localidades[i],"\n")
    else:
        print(lista[localidad_deseada],localidades[lista[localidad_deseada]])
    return

def lista_de_localidades():
    """Imprime un menu con la lista de localidades y los números de cada una"""
    print(
            "Localidades \n"
            "1. Usaquen \n" 
            "2. Engativa \n"
            "3. Fontibón \n"
            "4. Kennedy \n"
            "5. Suba \n"
            "6. Chapinero \n"
            "7. Ciudad Bolivar \n"
            "8. Barrios Unidos \n"
            "9. La Candelaria \n"
            "10. Rafael Uribe Uribe \n"
            "11. Puente Aranda \n"
            "12. Usme \n"
            "13. Teusaquillo \n"
            "14. Tunjuelito \n"
            "15. Bosa \n"
            "16. Fuera de Bogota \n"
            "17. Santa Fe \n"
            "18. Antonio Nariño \n"
            "19. San Cristóbal \n"
            "20. Los Martires \n"
            "21. Sin Dato \n"
            "22. Todas \n"
            )
    return
def contagio_por_localidad(lineas):
    """Crea diccionarios según la estadística que se desea conocer"""
    lista = ["Localidades","Usaquen","Engativa","Fontibón","Kennedy","Suba","Chapinero","Ciudad Bolivar","Barrios Unidos","La Candelaria","Rafael Uribe Uribe","Puente Aranda","Usme","Teusaquillo","Tunjuelito","Bosa","Fuera de Bogota","Santa Fe","Antonio Nariño","San Cristobal","Los Martires","Sin Dato","Todas"]
    while True:
        print(
        "\n"
        "Estadisticas por localidad \n"
        "1. Total de contagiados por localidad \n"
        "2. Casos por sexo en localidad \n"
        "3. Tipos de casos por localidad \n"
        "4. Tipo de ubicacion/residencia \n"
        "5. Rango de edades por contagio \n"
        "6. Estado de los contagiados por localidad \n"
        "7. Ver menu de estadísticas \n"
        "8. Volver al menú principal \n"
        )
        localidades = {}
        opcion = 0
        try:
            opcion = int(input("Ingrese la estadistica que desea conocer: "))
        except ValueError:
            print("Debe ingresar un número entero, por favor intentelo de nuevo \n")
            
        if opcion == 1:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = 0
                localidades[lineas[i][2]] += 1
            lista_de_localidades()
            elegir_localidad(lista, localidades)

        if opcion == 2:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = {}
                if lineas[i][4] not in localidades[lineas[i][2]]:
                    localidades[lineas[i][2]][lineas[i][4]] = 0
                localidades[lineas[i][2]][lineas[i][4]] += 1

            lista_de_localidades()

            elegir_localidad(lista, localidades)
        
        if opcion == 3:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = {}
                if lineas[i][5] not in localidades[lineas[i][2]]:
                    localidades[lineas[i][2]][lineas[i][5]] = 0
                localidades[lineas[i][2]][lineas[i][5]] += 1

            lista_de_localidades()

            elegir_localidad(lista, localidades)
        
        if opcion == 4:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = {}
                if lineas[i][6] not in localidades[lineas[i][2]]:
                    localidades[lineas[i][2]][lineas[i][6]] = 0
                localidades[lineas[i][2]][lineas[i][6]] += 1

            lista_de_localidades()

            elegir_localidad(lista, localidades)
                
        if opcion == 5:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = {}
                    localidades[lineas[i][2]]["menores de 18"] = 0
                    localidades[lineas[i][2]]["de 18 a 35"] = 0
                    localidades[lineas[i][2]]["de 36 a 55"] = 0
                    localidades[lineas[i][2]]["mayores de 56"] = 0

                if int(lineas[i][3]) < 18 :
                    localidades[lineas[i][2]]["menores de 18"] += 1
                if int(lineas[i][3]) > 18 and int(lineas[i][3]) <= 35:
                    localidades[lineas[i][2]]["de 18 a 35"] += 1
                if int(lineas[i][3]) > 35 and int(lineas[i][3]) <= 55:
                    localidades[lineas[i][2]]["de 36 a 55"] += 1
                if int(lineas[i][3]) > 55:
                    localidades[lineas[i][2]]["mayores de 56"] += 1

            lista_de_localidades()

            elegir_localidad(lista, localidades)

        if opcion == 6:
            for i in range(1, len(lineas)):
                if lineas[i][2] not in localidades:
                    localidades[lineas[i][2]] = {}
                if lineas[i][7] not in localidades[lineas[i][2]]:
                    localidades[lineas[i][2]][lineas[i][7]] = 0
                localidades[lineas[i][2]][lineas[i][7]] += 1

            lista_de_localidades()

            elegir_localidad(lista, localidades)

        if opcion == 7:
            print(
        "Que estadistica desea conocer \n"
        "1. Total de contagiados por localidad \n"
        "2. Casos por sexo en localidad \n"
        "3. Tipos de casos por localidad \n"
        "4. Tipo de ubicación/residencia \n"
        "5. Rango de edades por contagio \n"
        "6. Estado de los contagiados por localidad \n"
        "7. Ver menu de estadisticas \n"
        "8. Volver al menu principal"
    )
        if opcion == 8:

            return
