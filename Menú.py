import localidades
import fecha
import os
import estadisticas_por_caso
def leer_datos():
    """Abre el archivo Bogota_covid19.csv en modo lectura, posterior a esto crea una lista donde cada
    linea corresponde a un string, para luego crear una sublista por linea, pudiendo tomar los datos
    de cada linea individualmente"""
    with open("Bogota_covid19.csv","r") as tabla:
            lineas = tabla.read().splitlines()
            for i in range(len(lineas)):
                lineas[i] = lineas[i].split(",")
            borrarPantalla()

            return lineas

def borrarPantalla():
    """Funcion como su nombre lo indica para borrar pantalla, se utiliza la libreria os para que 
    esta funcion pueda ser ejecutada tanto en MAC-OS como en Windows y en Linux"""
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def main():
    ""
    while True:
        print(
    "Menu general \n"
    "1. leer datos \n"
    "2. estadisticas por localidad \n"
    "3. Contagiados por fecha \n"
    "4. fechas de mayor y menor contagio \n"
    "5. descargar tabla de estadisticas generales \n"
        )
        estadística = 0
        try:
            estadística = int(input("ingrese la estadistica que desea conocer: "))
        except ValueError:
            print("Por favor, ingrese una opcion valida")

        if estadística == 1:

            lineas = leer_datos()
            
        if estadística == 2:
            try:
                localidades.contagio_por_localidad(lineas)
            except NameError:
                print("Primero deben ser leidos los datos del archivo para que el programa funcione \n")
            
        if estadística == 3:
            try:
                fecha.niidea(lineas)
            except NameError:
                print("Primero deben ser leidos los datos del archivo para que el programa funcione \n")
        
        if estadística == 5:
            try:
                estadisticas_por_caso.main(lineas)
            except NameError:
                print("Primero deben ser leidos los datos del archivo para que el programa funcione \n")
main()