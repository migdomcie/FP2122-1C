'''
Created on 28 oct 2021

@author: Migue
'''
import csv
from collections import*
from datetime import datetime

Nacimientos= namedtuple("Nacimientos","Nombre,TipoCentro, Municipio, Provincia, FNacimiento, Hombres, Mujeres, PromedioPesoH, PromedioPesoM, PromedioAltH, PromedioAltM")

def lee_registros(fichero):
    lista_registros=[]
    with open(fichero, encoding="utf-8") as f:
        lector= csv.reader(f)
        next(lector)
        for Nombre,TipoCentro, Municipio, Provincia, FNacimiento, Hombres, Mujeres, PromedioPesoH, PromedioPesoM, PromedioAltH, PromedioAltM in lector:
            tupla= Nacimientos(Nombre, TipoCentro, Municipio, Provincia, datetime.strptime(FNacimiento, "%d/%m/%Y"), int(Hombres), int(Mujeres), float(PromedioPesoH), float(PromedioPesoM), float(PromedioAltH), float(PromedioAltM))
            lista_registros.append(tupla)
            
    return lista_registros 
            

