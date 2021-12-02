# -*- coding: utf-8 -*-
'''
Created on 28 oct 2021

@author: Migue
'''
import csv
from collections import*
from datetime import datetime
from nacimientos import*


#FUNCIONES SECUNDARIAS DEFINIDAS 
   
### BLOQUE 1
#FUNCION TIPO 1

def test_filtra_nacimientos_provincias():
    print("#" * 15, "TEST de filtra_nacimientos_provincias", "#" * 15)
    provincia= "Sevilla"
    datos_filtrados_provincia= filtra_nacimientos_provincias(registros, provincia)
    print(f"\n \tLos nacimientos de la provincia de {provincia} son los siguientes:\n \n\t---> {datos_filtrados_provincia}\n")
    
#FUNCION TIPO 3

def test_calcula_pesopromedio_género_provincias():
    print("#" * 15, "TEST de calcula_pesopromedio_género_provincias", "#" * 15)
    provincia= "Cádiz"
    género= "Hombre"
    pesopromedio_por_provincias_género= calcula_pesopromedio_género_provincias(registros, provincia, género)
    print (f"\n \tEl promedio de peso del género de '{género}' en {provincia} es de {pesopromedio_por_provincias_género:.3f} kg\n")

### BLOQUE 2
#FUNCION TIPO 4

def test_calcula_altura_max_género_tipocentro():
    print("#" * 15, "TEST de calcula_altura_max_género_tipocentro", "#" * 15)
    tipocentro= "Hospital de especialidades"
    género= "Mujer" 
    alturas_max_género_tipocentro= calcula_altura_max_género_tipocentro(registros, tipocentro, género)
    print(f"\n \tLa estatura máxima para el género de '{género}' en el hospital de tipo '{tipocentro}' es de {alturas_max_género_tipocentro} cm\n")
    
#FUNCION TIPO 6

def test_filtra_recientes_nacimientos_género_provincias():
    print("#" * 15, "TEST de filtra_recientes_nacimientos_género_provincias ", "#" * 15)
    provincia= "Málaga"
    género= "Hombre"
    nacimientos_recientes_filtrados= filtra_recientes_nacimientos_género_provincias(registros, provincia, género)
    print(f"\n \tLos nacimientos más recientes del género de '{género}' producidos en {provincia} son los siguientes:\n \n\t---> {nacimientos_recientes_filtrados}\n")

#FUNCION TIPO 7

def test_filtra_dict_nacimientos_tipocentro_mes():
    print("#" * 15, "TEST de filtra_dict_nacimientos_tipo_centro_mes ", "#" * 15)
    tipocentro= "Hospital regional"
    mes= "enero"
    dict_nacimientos_tipocentro_mes= filtra_dict_nacimientos_tipocentro_mes(registros, tipocentro, mes)
    print(f"\n \tLos nacimientos producidos en el mes de {mes} en el hospital de tipo '{tipocentro}' son los siguientes:\n \n\t---> {dict_nacimientos_tipocentro_mes}\n")
    
#FUNCIÓN LECTURA DEFINIDA

def test_lee_registros():
    datos= lee_registros("../data/nacimientos.csv")
    return datos

#FUNCIÓN LECTURA (TEST)

registros= test_lee_registros()
print("\n \tHay en total", len(registros), "registros")
print("\n \tLos tres primeros registros:", registros[:3])
print("\n \tLos tres últimos registros:", registros[-3:],"\n")


#FUNCIONES SECUNDARIAS (TESTS)

test_filtra_nacimientos_provincias() 
test_calcula_pesopromedio_género_provincias() 
test_calcula_altura_max_género_tipocentro()   
test_filtra_recientes_nacimientos_género_provincias()  
test_filtra_dict_nacimientos_tipocentro_mes()  

