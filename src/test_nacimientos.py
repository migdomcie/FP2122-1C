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

def test_dict_filtra_nacimientos_tipocentro_mes():
    print("#" * 15, "TEST de dict_filtra_nacimientos_tipo_centro_mes ", "#" * 15)
    tipocentro= "Hospital regional"
    mes= "enero"
    dict_nacimientos_tipocentro_mes= dict_filtra_nacimientos_tipocentro_mes(registros, tipocentro, mes)
    print(f"\n \tLos nacimientos producidos en el mes de {mes} en el hospital de tipo '{tipocentro}' son los siguientes:\n \n\t---> {dict_nacimientos_tipocentro_mes}\n")

### BLOQUE 3
#FUNCION TIPO 8

def test_dict_cuenta_numero_nacimientos_por_hospital():
    print("#" * 15, "TEST de dict_cuenta_numero_nacimientos_por_hospital", "#" * 15)
    print(f"\n \tLos nacimientos producidos por hospital son los siguientes:\n \n\t---> {dict_cuenta_numero_nacimientos_por_hospital (registros)}\n")

#FUNCION TIPO 11

def test_dict_calcula_altura_promedio_por_hospital():
    print("#" * 15, "TEST de dict_calcula_altura_promedio_por_hospital", "#" * 15)
    print(f"\n \tLas alturas promedio (en cm) por cada uno de los hospitales son las siguientes:\n \n\t---> {dict_calcula_altura_promedio_por_hospital(registros)}\n")

#FUNCION TIPO 12

def test_dict_calcula_porcentaje_nacimientos_por_género_provincia():
    print("#" * 15, "TEST de dict_calcula_porcentaje_nacimientos_por_género_provincia", "#" * 15)
    print(f"\n \tLos porcentajes (%) de nacimientos en cada provincia por género (hombre y mujer, resp.) respecto del total de nacimientos, son los siguientes:\n \n\t---> {dict_calcula_porcentaje_nacimientos_por_género_provincia(registros)}\n")
  
#FUNCION TIPO 13

def test_dict_calcula_nacimientos_menor_peso_por_municipio():
    print("#" * 15, "TEST de dict_calcula_nacimientos_menor_peso_por_municipio", "#" * 15)
    n= 5
    print(f"\n \tLos {n} nacimientos por municipio ordenados de menor a mayor peso (en kg) son los siguientes:\n \n \t {dict_calcula_nacimientos_menor_peso_por_municipio(registros, n)}\n")

#FUNCIÓN DEFENSA
def test_pesos_por_municipios():
    print("#" * 15, "TEST de pesos_por_municipios(datos)", "#" * 15)
    print(f"\n \tLos pesos por municipios son los siguientes:\n \n \t {pesos_por_municipios(registros)}\n")

### BLOQUE 4
#FUNCION DE USO DE MATPLOTLIB

#FUNCION EXTRA PARA USO DE MATPLOTLIB

def test_dict_nacimientos_por_mes():
    print("#" * 15, "TEST de dict_nacimientos_por_mes (función extra)", "#" * 15)
    print(f"\n \tLos nacimientos totales producidos en cada mes son los siguientes:\n \n \t {dict_nacimientos_por_mes(registros)}\n")
    
#FUNCION DE GRAFICA

def test_grafica_nacimientos_por_mes():
    etiquetas= list(dict_nacimientos_por_mes(registros).keys())
    valores= list(dict_nacimientos_por_mes(registros).values())
    titulo= "Nacimientos totales producidos en cada mes"
    etiqueta_eje_x= "Meses"
    etiqueta_eje_y= "Nº nacimientos"
    print("#" * 15, "TEST de grafica_nacimientos_por_mes", "#" * 15)
    print(f"\n \t {grafica_nacimientos_por_mes(etiquetas, valores, titulo, etiqueta_eje_x=None,etiqueta_eje_y=None)}\n")

#FUNCION LECTURA DEFINIDA

def test_lee_registros():
    datos= lee_registros("../data/nacimientos.csv")
    return datos

#FUNCION LECTURA (TEST)

registros= test_lee_registros()
print("\n \tHay en total", len(registros), "registros")
print("\n \tLos tres primeros registros:", registros[:3])
print("\n \tLos tres últimos registros:", registros[-3:],"\n")


#FUNCIONES SECUNDARIAS (TESTS)

test_filtra_nacimientos_provincias() 
test_calcula_pesopromedio_género_provincias() 
test_calcula_altura_max_género_tipocentro()   
test_filtra_recientes_nacimientos_género_provincias()  
test_dict_filtra_nacimientos_tipocentro_mes()
test_dict_cuenta_numero_nacimientos_por_hospital()
test_dict_calcula_altura_promedio_por_hospital()
test_dict_calcula_porcentaje_nacimientos_por_género_provincia()
test_dict_calcula_nacimientos_menor_peso_por_municipio()
test_pesos_por_municipios()
test_dict_nacimientos_por_mes()
test_grafica_nacimientos_por_mes()

