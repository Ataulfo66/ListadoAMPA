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
#print(longitud)
# Verificar qeu tengo la variable cadenacruda como objeto tipo string
#print(cadenacruda)
finIO = 0
#Crea un fichero llamado tabla.txt en el que se irán escribiendo los datos ordenados
tabla = open("tabla.txt","w")
#Crea el encabezamiento de la tabla
tabla.write("Nombre;telefono;email;Cuota\n")
while finIO < (longitud - 10):
    #Busca en cadenacruda el siguiente 'BEGIN:VCARD'
    posini = cadenacruda.find('BEGIN:VCARD', finIO)
    #Busca el nombre
    posFN = cadenacruda.find('FN:', posini)
    posFN_ = cadenacruda.find('\n', posFN)
    #Escribe el nombre en el fichero tabla.txt
    tabla.write(cadenacruda[posFN+3:posFN_]+';')
    #Busca el telefono
    posTEL = cadenacruda.find('TEL', posini)
    posTELc = cadenacruda.find(':', posTEL)
    posTEL_ = cadenacruda.find('\n', posTEL)
    #Escribe el correo electrónico en el fichero tabla.txt
    tabla.write(cadenacruda[posTELc+1:posTEL_]+';')
    #Busca el correo electrónico
    posEMAIL = cadenacruda.find('EMAIL', posini)
    posEMAILc = cadenacruda.find(':', posEMAIL)
    posEMAIL_ = cadenacruda.find('\n', posEMAIL)
    #Escribe el correo electrónico en el fichero tabla.txt
    tabla.write(cadenacruda[posEMAILc+1:posEMAIL_]+';\n')
    finIO = cadenacruda.find('END:VCARD', posini)
tabla.close()