
def descargar_estadisticas_caso(datos, nombre_archivo):
    encabezado = ['','F','','','','F Total','M','','','','M Total']
    pegamento = ','
    archivo = open(nombre_archivo,'w')
    archivo.write(pegamento.join(encabezado)+'\n')
    encabezado = ['Localidad','Desconocido','En estudio','Importado','Relacionado','','Desconocido','En estudio','Importado','Relacionado','']
    
    archivo.write(pegamento.join(encabezado)+'\n')
    


def main(lineas):
    '''crea un diccionario para localidades, posterior a esto uno dentro del mismo que dividirá los casos por sexo,
    y luego, dentro de este se colocará un tercer diccionario con los tipos de casos, de esta forma los casos quedan separados
    con 3 filtros a la vez, localidad, sexo y tipo'''
    estudiantes = 0

    localidades = {}

    for i in range(1, len(lineas)):
        if lineas[i][2] not in localidades:
            localidades[lineas[i][2]] = {}
        if lineas[i][4] not in localidades[lineas[i][2]]:
            localidades[lineas[i][2]][lineas[i][4]] = {}
        if lineas[i][5] not in localidades[lineas[i][2]][lineas[i][4]]:
            localidades[lineas[i][2]][lineas[i][4]][lineas[i][5]] = 0
        localidades[lineas[i][2]][lineas[i][4]][lineas[i][5]] += 1
        
    print(localidades)
