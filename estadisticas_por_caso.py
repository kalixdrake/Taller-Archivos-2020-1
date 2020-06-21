
def descargar_estadisticas_caso(datos, nombre_archivo):
    encabezado = ['','F','','','','F Total','M','','','','M Total']
    pegamento = ','
    archivo = open(nombre_archivo,'w')
    archivo.write(pegamento.join(encabezado)+'\n')
    encabezado = ['Localidad','Desconocido','En estudio','Importado','Relacionado','','Desconocido','En estudio','Importado','Relacionado','']
    
    archivo.write(pegamento.join(encabezado)+'\n')
    


def main():
    estudiantes = 0
    descargar_estadisticas_caso(estudiantes, 'archivos/estadisticas_caso.csv')
main()