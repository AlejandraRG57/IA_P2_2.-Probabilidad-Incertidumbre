#Alejandra Rodriguez Guevara 21310127 6E1

#La extracción de información es un proceso mediante el cual se identifican y se recuperan datos específicos de un conjunto de datos más grande. 

import re

#Texto de ejemplo.
texto = "La reunión está programada para el 25 de abril de 2022."

#Expresión regular para identificar fechas en formato dd de mmmm de aaaa.
patron_fecha = r'\b(\d{1,2}) de (\w+) de (\d{4})\b'

#Buscamos todas las fechas en el texto.
fechas_encontradas = re.findall(patron_fecha, texto)

#Imprimimos las fechas encontradas.
print("Fechas encontradas:")
for fecha in fechas_encontradas:
    print("- {}/{}/{}".format(fecha[0], fecha[1], fecha[2]))