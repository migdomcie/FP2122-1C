# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 2021-2022)
**Autor/a:** Miguel Ángel Domínguez Ciero ; **uvus:** migdomcie


Este proyecto ha sido realizado con base en conjuntos de datos que abarcan, con grandes detalles, una secuencia de varios de los últimos nacimientos producidos en distintos hospitales de Andalucía. Su objetivo es el desarrollo de un programa capacitado para el óptimo tratamiento y gestión de datos en función de lo que el usuario (supongamos, en este caso, un funcionario) desee conocer para su posterior uso.

Concretamente, trabajaremos con datos específicos del hospital (registros) acerca de los recientes nacimientos, siendo éstos de la índole de especificaciones del hospital de nacimiento, el lugar y fecha de nacimiento, así como otros datos descriptivos físicos de los nacidos en función de su sexo.

    
## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **nacimientos.py**: Contiene funciones para trabajar con los datos de los nacimientos.
    * **test_nacimientos.py**: Contiene funciones de test para probar las funciones del módulo "nacimientos.py".
    
* **/data**: Contiene el dataset o datasets del proyecto
    * **nacimientos.csv**: Archivos con los datos de los nacimientos en hospitales andaluces con los que vamos a trabajar.
    
    
## Estructura del *dataset*

El dataset con el que vamos a trabajar recoge los distintos registros de un hospital distinto, para el cual supondrá una fila concreta. En cada una de estas filas existirán los correspondientes datos que tienen como título los niños nacidos en cada uno de dichos hospitales, estando cada fila formadas por 11 columnas, con la siguiente descripción:

* **Nombre**: de tipo str, representa el nombre propio del hospital en cuestión 
* **Tipo de Centro**: de tipo str, representa el tipo de hospital en cuestión 
* **Municipio**: de tipo str, representa el municipio en que está ubicado el hospital en cuestión
* **Provincia**: de tipo str, representa la provincia donde se ubica el hospital en cuestión
* **Fecha de nacimiento**: de tipo datetime.date representa el día de nacimiento de los nacidos
* **Hombres**: de tipo int, representa el número de niños nacidos en dicho hospital
* **Mujeres**: de tipo int, representa el número de niñas nacidos en dicho hospital
* **Promedio Peso Hombres (kg)**: de tipo float, representa el promedio del peso de los niños nacidos en dicho hospital
* **Promedio Peso Mujeres (kg)**: de tipo float representa el promedio del peso de las niñas nacidas en dicho hospital
* **Promedio estatura (cm)**: de tipo float, representa el promedio de la estatura de los niños nacidos en dicho hospital 
* **Promedio estatura (cm)**: de tipo float, representa el promedio de la estatura de las niñas nacidas en dicho hospital


## Tipos implementados



Para trabajar con los datos del dataset, ha sido definida la siguiente namedtuple:

`Nacimientos= namedtuple("Nacimientos","Nombre,TipodeCentro, Municipio, Provincia, FechadeNacimiento, Hombres, Mujeres, PromedioPesoH, PromedioPesoM, PromedioEstaturaH, PromedioEstaturaM")`

en la que los tipos de cada uno de los campos son los siguientes:

`Nacimientos(str, str, str, str, datetime.date, str, str, float, float, float, float)`


## Funciones implementadas

En este proyecto se han implementado las siguientes funciones que corresponden a los módulos indicados a continuación. Dichas funciones se encuentran clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas. El módulo principal se trata del módulo **nacimientos.py**, donde se ubicarán varios de los bloques, los cuales comprenderan varias de las funciones destinadas a cada entrega.

### Módulo nacimientos

#### Entrega 1

* **Bloque 0**  

     * **lee_registros(fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas con los datos del fichero.
   
### Módulo test_nacimientos

En este módulo se han definido las siguientes funciones, las cuales son usadas para probar la función cuyo nombre posee. Por ejemplo, la función **test_lee_registros** prueba la función **lee_registros**.

* **test_lee_registros(fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas con los datos del fichero.
