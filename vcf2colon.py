# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:48:30 2017

@author: rmcarreras
"""

# Abrir el fichero contacts.vcf y darle el nombre contactos
contactos = open("contacts.vcf", "r")
#convertir el objeto contactos en una cadena de texto
cadenacruda = contactos.read()
contactos.close()
longitud = len(cadenacruda)
print(longitud)
# Verificar qeu tengo la variable cadenacruda como objeto tipo string
#print(cadenacruda)

#Crea un fichero llamado tabla.txt en el que se irán escribiendo los datos ordenados
tabla = open("tabla.txt","w")
#Crea el encabezamiento de la tabla
tabla.write("Nombre;telefono;email;Cuota\n")
posini = cadenacruda.find('BEGIN:VCARD')
#Busca en cadenacruda el siguiente 'BEGIN:VCARD'

posfin = cadenacruda.find('END:VCARD')
print(posini,posfin)
posini2 = cadenacruda.find('BEGIN:VCARD', posini)
print(posini,posfin, posini2)
tabla.close()