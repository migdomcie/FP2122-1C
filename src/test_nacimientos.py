'''
Created on 28 oct 2021

@author: Migue
'''
from nacimientos import*


#Lectura
def test_lee_registros(fichero,lim_inf=0, lim_sup=-1, paso=1):
    datos= lee_registros(fichero)
    res= datos[lim_inf:lim_sup:paso]
    return res

#tests
print(test_lee_registros("../data/nacimientos.csv", lim_sup=3))

