import datetime
import localidades
def validar_fechas():
    rango_fechas = []
    fecha_1 = input("Ingrese la fecha numero 1 en formato dd/mm/aaaa: ")
    if (int(fecha_1[:1]) > 29 and int(fecha_1[3:4]) == 2) or int(fecha_1[:1])<1 or int(fecha_1[:1])>31 or len(fecha_1[:1])>2 or int(fecha_1[3:4])<1 or int(fecha_1[3:4])>12:
        print("Fecha no valida, por favor ingrese una fecha existente \n")
        fecha_1 = input("Ingrese la fecha numero 1 en formato dd/mm/aaaa: ")
    else:
        fecha_1 = datetime.datetime(int(fecha_1[6:]),int(fecha_1[3:4]),int(fecha_1[:1]))
        

def niidea(lineas):
    
    lineas_ordenadas = sorted(lineas)
    contagiados = 0
    for i in range(len(lineas_ordenadas)):
        if fecha_1 == lineas_ordenadas[i][0]:
            contagiados += 1
        if fecha_2 == lineas_ordenadas[i][0]:
            contagiados += 1
    print("los contagiados entre",fecha_1,"y",fecha_2,"fueron:",contagiados)

