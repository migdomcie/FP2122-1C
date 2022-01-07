# -*- coding: utf-8 -*-
'''
Created on 28 oct 2021

@author: Migue
'''
import csv
from collections import*
from datetime import datetime
from matplotlib import*
import matplotlib.pyplot as plt

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
        
def dict_filtra_nacimientos_tipocentro_mes (datos, tipocentro, mes):
    dict_nacimientos_tipocentro_mes= dict()
    registro_tipocentro_mes= list()
    for registro in datos:
        if tipocentro == registro.TipoCentro and convierte_mesnom_mesnum(mes) == datetime.strftime(registro.FNacimiento, "%m"):
            registro_tipocentro_mes.append(registro)
            
        dict_nacimientos_tipocentro_mes[(mes,tipocentro)]= registro_tipocentro_mes
    
    return dict_nacimientos_tipocentro_mes

### BLOQUE 3
#FUNCION TIPO 8

def dict_cuenta_numero_nacimientos_por_hospital (datos):
    lista_hospitales= [registro.Nombre for registro in datos]
    dic= dict(Counter(lista_hospitales))       
    return dic 

#FUNCION TIPO 11

def dict_calcula_altura_promedio_por_hospital(datos): 
    dic_aux= dict()  
    contador= dict()
    lista= list()
    for registro in datos:
        if registro.Nombre not in dic_aux and (registro.PromedioAltH != 0 and registro.PromedioAltM == 0):
            dic_aux[registro.Nombre]= registro.PromedioAltH
            contador[registro.Nombre]= 1              
        
        elif registro.Nombre not in dic_aux and (registro.PromedioAltH == 0 and registro.PromedioAltM != 0):
            dic_aux[registro.Nombre]= registro.PromedioAltM
            contador[registro.Nombre]= 1
        
        elif registro.Nombre not in dic_aux and (registro.PromedioAltH != 0 and registro.PromedioAltM !=0):
            dic_aux[registro.Nombre]= registro.PromedioAltH
            dic_aux[registro.Nombre]= registro.PromedioAltM
            contador[registro.Nombre]= 2
          
        elif registro.Nombre in dic_aux and (registro.PromedioAltH != 0 and registro.PromedioAltM == 0):
            dic_aux[registro.Nombre]+= registro.PromedioAltH
            contador[registro.Nombre]+= 1
                          
        elif registro.Nombre in dic_aux and (registro.PromedioAltH == 0 and registro.PromedioAltM != 0):
            dic_aux[registro.Nombre]+= registro.PromedioAltM
            contador[registro.Nombre]+= 1
        
        elif registro.Nombre in dic_aux and(registro.PromedioAltH !=0 and registro.PromedioAltM != 0):
            dic_aux[registro.Nombre]+= registro.PromedioAltH
            dic_aux[registro.Nombre]+= registro.PromedioAltM
            contador[registro.Nombre]+= 2
        else:
            pass

    dic= {clave: "%.3f" %(valor/v) for clave, valor, v in zip(dic_aux.keys(), dic_aux.values(), contador.values())}
    
    return dic
    
#FUNCION TIPO 12

def dict_calcula_porcentaje_nacimientos_por_género_provincia(datos):
    dic_auxH= dict()
    dic_auxM= dict()
    
    for registro in datos:
        if registro.Provincia not in dic_auxH and registro.Hombres != 0:
            dic_auxH[registro.Provincia]= registro.Hombres
           
        elif registro.Provincia not in dic_auxM and registro.Mujeres != 0:
            dic_auxM[registro.Provincia]= registro.Mujeres
            
        elif registro.Provincia in dic_auxH and registro.Hombres != 0:
            dic_auxH[registro.Provincia]+= registro.Hombres
            
        elif registro.Provincia in dic_auxM and registro.Mujeres != 0:
            dic_auxM[registro.Provincia]+= registro.Mujeres
            
        else:
            pass
    
    contador= sum((list(dic_auxH.values()) + list(dic_auxM.values())))
    
    dic= {clave: (round((hombres/contador)*100,3), round((mujeres/contador)*100,3)) for clave, hombres, mujeres,  in zip(dic_auxH.keys(),dic_auxH.values(), dic_auxM.values())}
    
    return dic

#FUNCION TIPO 13

def dict_calcula_nacimientos_menor_peso_por_municipio(datos, n):
    dic_aux= {}
       
    for registro in datos:                                                                      
        if registro.Municipio not in dic_aux and (registro.PromedioPesoH != 0 and registro.PromedioPesoM != 0):
            dic_aux[registro.Municipio]= [registro.PromedioPesoH]
            dic_aux[registro.Municipio]+= [registro.PromedioPesoM]
            
        elif registro.Municipio not in dic_aux and (registro.PromedioPesoH != 0 and registro.PromedioPesoM == 0):                                      
            dic_aux[registro.Municipio]= [registro.PromedioPesoH]
        
        elif registro.Municipio not in dic_aux  and (registro.PromedioPesoH == 0 and registro.PromedioPesoM != 0):
            dic_aux[registro.Municipio]= [registro.PromedioPesoM]
            
        elif registro.Municipio in dic_aux and (registro.PromedioPesoH != 0 and registro.PromedioPesoM != 0):
            dic_aux[registro.Municipio]+= [registro.PromedioPesoH]
            dic_aux[registro.Municipio]+= [registro.PromedioPesoM]
        
        elif registro.Municipio in dic_aux and (registro.PromedioPesoH != 0 and registro.PromedioPesoM == 0):
            dic_aux[registro.Municipio]+= [registro.PromedioPesoH]
        
        elif registro.Municipio in dic_aux  and (registro.PromedioPesoH == 0 and registro.PromedioPesoM != 0):
            dic_aux[registro.Municipio]+= [registro.PromedioPesoM]
        
        else:
            pass
    
    lista_pesos_ordenados_provincia= [sorted(set(lista)) for lista in dic_aux.values()]
    
    dic= {clave: valor[:n] for clave, valor in zip(dic_aux.keys(), lista_pesos_ordenados_provincia)}

    return dic

### BLOQUE 4
#FUNCION DE USO DE MATPLOTLIB

def convierte_mesnum_mesnom(mes):
    meses= {"01":"enero", "02":"febrero", "03":"marzo", "04": "abril", "05": "mayo" , "06": "junio" , "07":"julio" , "08": "agosto", "09": "septiembre", "10": "octubre", "11": "noviembre","12": "diciembre"} 
    mes_correspond= None
    for m in meses:
        if mes in list(meses.keys()):
            mes_correspond= meses[mes]
            
    return mes_correspond

def dict_nacimientos_por_mes(datos):
    dic_aux= {}
    for registro in datos:
        if datetime.strftime(registro.FNacimiento, "%m") not in dic_aux:
            dic_aux[datetime.strftime(registro.FNacimiento, "%m")]= 1
            
        else:
            dic_aux[datetime.strftime(registro.FNacimiento, "%m")]+= 1
    
    dic= {convierte_mesnum_mesnom(clave): valor for clave, valor in dic_aux.items()}  
    
    return dic

def grafica_nacimientos_por_mes(etiquetas, valores, titulo, etiqueta_eje_x=None,etiqueta_eje_y=None):
    plt.title(titulo, fontsize=16)
    indice = range(len(etiquetas))
    plt.bar(indice, valores)
    plt.xticks(indice, etiquetas, fontsize=8)
    plt.xlabel (etiqueta_eje_x)
    plt.ylabel (etiqueta_eje_y)
    plt.show() 

