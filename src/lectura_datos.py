'''
Created on 26 oct 2021

@author: Migue
'''
import csv



def lee_registros(fichero):
    lista_tuplas_registros=[]
    res= lista_tuplas_registros
    with open(fichero, encoding="utf-8") as f:
        lector= csv.reader(f)
        next(lector)
        for registro in fichero:
            res.append(registro)
            print (registro)
    return res  
            
lee_registros("../data/Nacimientos.csv")
   