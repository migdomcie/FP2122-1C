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
    
def test_filtra_nacimientos_provincias():
    print("#" * 15, "TEST de filtra_nacimientos_provincias", "#" * 15)
    provincia= input("\n \tEscriba la provincia en que desea filtrar los datos --->")
    datos_filtrados_provincia= filtra_nacimientos_provincias(registros, provincia)
    print(f"\n \t--->Los nacimientos de la provincia de {provincia} son los siguientes:\n \n {datos_filtrados_provincia}")
    
def test_calcula_pesopromedio_género_provincias():
    print("#" * 15, "TEST de calcula_pesopromedio_género_provincias", "#" * 15)
    provincia= input("\n \tEscriba la provincia en que desea filtrar los datos --->")
    género= input("\n \tEscriba el género para el que desea filtrar los datos --->")
    pesopromedio_por_provincias_género= calcula_pesopromedio_género_provincias(registros, provincia, género)
    print (f"\n \t--->El promedio de peso del género de {género} en {provincia} es de {pesopromedio_por_provincias_género} kg")

def test_calcula_altura_max_género_tipocentro():
    print("#" * 15, "TEST de calcula_altura_max_género_tipocentro", "#" * 15)
    tipocentro= input("\n \tEscriba el tipo de centro para el que desea filtrar los datos --->")
    género= input("\n \tEscriba el género para el que desea filtrar los datos --->") 
    alturas_max_género_tipocentro= calcula_altura_max_género_tipocentro(registros, tipocentro, género)
    print(f"\n \t--->La estatura máxima para el género de {género} en el hospital de tipo: {tipocentro} es de {alturas_max_género_tipocentro} cm")
    
def test_filtra_recientes_nacimientos_género_provincias():
    print("#" * 15, "TEST de filtra_recientes_nacimientos_género_provincias ", "#" * 15)
    provincia= input("\n \tEscriba la provincia en que desea filtrar los datos --->")
    género= input("\n \tEscriba el género para el que desea filtrar los datos --->")
    nacimientos_recientes_filtrados= filtra_recientes_nacimientos_género_provincias(registros, provincia, género)
    print(f"\n \t--->Los nacimientos más recientes del género de {género} producidos en {provincia} son los siguientes:\n \n {nacimientos_recientes_filtrados}")

def test_filtra_dict_nacimientos_tipocentro_mes():
    print("#" * 15, "TEST de filtra_dict_nacimientos_tipo_centro_mes ", "#" * 15)
    tipocentro= input("\n \tEscriba el tipo de centro para el que desea filtrar los datos --->")
    mes= input("\n \tEscriba el mes para el que desea filtrar los datos --->")
    dict_nacimientos_tipocentro_mes= filtra_dict_nacimientos_tipocentro_mes(registros, tipocentro, mes)
    print(f"\n \t--->Los nacimientos producidos en el mes {mes} en el hospital de tipo: {tipocentro} son los siguientes:\n \n {dict_nacimientos_tipocentro_mes}")
    
#FUNCIÓN LECTURA DEFINIDA

def test_lee_registros():
    datos= lee_registros("../data/Nacimientos.csv")
    return datos

#FUNCIÓN LECTURA (TEST)

registros= test_lee_registros()
'''
print("\n \tHay en total", len(registros), "registros")
print("\n \tLos tres primeros registros:", registros[:3])
print("\n \tLos tres últimos registros:", registros[-3:])
'''

#FUNCIONES SECUNDARIAS (TESTS)

#test_filtra_nacimientos_provincias() 
#test_calcula_pesopromedio_género_provincias() 
#test_calcula_altura_max_género_tipocentro()   
#test_filtra_recientes_nacimientos_género_provincias()  
#test_filtra_dict_nacimientos_tipocentro_mes()  
