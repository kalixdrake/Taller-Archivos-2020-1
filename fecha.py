def validar_fechas():
    fecha_1 = []
    fecha_2 = []
    entrada_1 = input("Porfavor ingrese el dia de la fecha inicial: ")
    if int(entrada_1)<1 or int(entrada_1)>31 or len(entrada_1)>2:
        print("Porfavor ingrese un dia valido ")
        entrada_1 = input("Porfavor ingrese el dia de la fecha inicial: ")
    entrada_2 = input("Porfavor ingrese fecha final en formato dd/mm/aaa")
def niidea(lineas):
    
    lineas_ordenadas = sorted(lineas)
    contagiados = 0
    for i in range(len(lineas_ordenadas)):
        if fecha_1 == lineas_ordenadas[i][0]:
            contagiados += 1
        if fecha_2 == lineas_ordenadas[i][0]:
            contagiados += 1
    print("los contagiados entre",fecha_1,"y",fecha_2,"fueron:",contagiados)
