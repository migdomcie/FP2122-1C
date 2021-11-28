# -*- coding: utf-8 -*-
'''
Created on 28 oct 2021

@author: Migue
'''
import csv
from collections import*
from datetime import datetime


Nacimientos= namedtuple("Nacimientos","Nombre,TipoCentro, Municipio, Provincia, FNacimiento, Hombres, Mujeres, PromedioPesoH, PromedioPesoM, PromedioAltH, PromedioAltM")


def lee_registros(fichero):
    with open(fichero, encoding="utf-8") as f:
        lector= csv.reader(f)
        next(lector)
        lista_nacimientos= list()
        for Nombre,TipoCentro, Municipio, Provincia, FNacimiento, Hombres, Mujeres, PromedioPesoH, PromedioPesoM, PromedioAltH, PromedioAltM in lector:
            tupla= Nacimientos(Nombre, TipoCentro, Municipio, Provincia, datetime.strptime(FNacimiento, "%d/%m/%Y"), int(Hombres), int(Mujeres), float(PromedioPesoH), float(PromedioPesoM), float(PromedioAltH), float(PromedioAltM))
            lista_nacimientos.append(tupla)
            
    return lista_nacimientos

### BLOQUE 1
#FUNCION TIPO 1

def filtra_nacimientos_provincias(datos, provincia):
    registro_provincias= [registro for registro in datos if provincia == registro.Provincia]
    return registro_provincias   

 
#FUNCION TIPO 3

def calcula_pesopromedio_género_provincias (datos, provincia, género): 
    promedio_peso_provincias= list()
    
    for registro in datos:
        if provincia == registro.Provincia and género == "Hombre" and registro.Hombres != 0:
            promedio_peso_provincias.append(registro.PromedioPesoH)
    
        elif provincia == registro.Provincia and género == "Mujer" and registro.Mujeres != 0:
            promedio_peso_provincias.append(registro.PromedioPesoM)
                   
    return (sum(promedio_peso_provincias) / len(promedio_peso_provincias))


### BLOQUE 2
#FUNCION TIPO 4
 
def calcula_altura_max_género_tipocentro (datos, tipocentro, género):
    alturas_género_centro= list()
    for registro in datos:
        if tipocentro == registro.TipoCentro and (género == "Hombre" and registro.Hombres !=0):    
            alturas_género_centro.append(registro.PromedioAltH)
        
        elif tipocentro == registro.TipoCentro and (género == "Mujer" and registro.Mujeres !=0):
            alturas_género_centro.append(registro.PromedioAltM)
            
    maximo_alturas_género_centro= max(alturas_género_centro)   
     
    return maximo_alturas_género_centro


#FUNCION TIPO 6

def filtra_recientes_nacimientos_género_provincias (datos, provincia, género):
    registros_provincia_género= list()
    for registro in datos:
        if provincia == registro.Provincia and género == "Hombre":
            registros_provincia_género.append(registro)
            
        elif provincia == registro.Provincia and género == "Mujer":
            registros_provincia_género.append(registro)
            
    registros_ordenados_edad= sorted(registros_provincia_género, key=lambda registro: registro.FNacimiento, reverse=True)
    
    return registros_ordenados_edad
    
     
#FUNCION TIPO 7

def convierte_mesnom_mesnum(mes):
    meses= {"enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06", "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11","diciembre": "12"} 
    mes_correspond= None
    for m in meses:
        if mes in list(meses.keys()):
            mes_correspond= meses[mes]
            
    return mes_correspond
        
def filtra_dict_nacimientos_tipocentro_mes (datos, tipocentro, mes):
    dict_nacimientos_tipocentro_mes= dict()
    registro_tipocentro_mes= list()
    for registro in datos:
        if tipocentro == registro.TipoCentro and convierte_mesnom_mesnum(mes) == datetime.strftime(registro.FNacimiento, "%m"):
            registro_tipocentro_mes.append(registro)
            
        dict_nacimientos_tipocentro_mes[f"Nacimientos en {mes} para el tipo: {tipocentro}"]= registro_tipocentro_mes
    
    return dict_nacimientos_tipocentro_mes
       
