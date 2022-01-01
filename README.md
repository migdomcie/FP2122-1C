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
     
#### Entrega 2

 * **Bloque 1**
 
    * **filtra_nacimientos_provincias (datos, provincia)**: Dada una lista de tuplas de tipo Nacimientos y una provincia, facilitada como parámetro, devuelve una lista de tuplas de tipo Nacimientos con los datos de los nacimientos producidos en tal provincia.
     
    * **calcula_pesopromedio_género_provincias (datos, provincia, género)**: Dada una lista de tuplas de tipo Nacimientos, una provincia y el género como parámetros, devuelve el promedio de peso de los nacimientos producidos en dicha provincia y para dicho género.
     
 
 * **Bloque 2**
     
     * **calcula_altura_max_género_tipocentro (datos, tipocentro, género)**: Dada una lista de tuplas de tipo Nacimientos, el tipo de centro y el género devuelve la tupla procedente de dicha lista que consiste en el nacimiento de altura máxima por tipo de centro y género facilitados como parámetros.
     
     * **filtra_recientes_nacimientos_género_provincias (datos, provincia, género)**: Dada una lista de tuplas de tipo Nacimientos, la provincia y el género facilitados como parámetros, devuelve la lista de tuplas ordenadas con los nacimientos de más recientes a menos recientes por provincia y género.
     
     * **convierte_mesnom_mesnum(datos, mes)**: Función auxiliar que convierte el mes en nombre aportado como parámetro, a mes en número para poder compararlo con el mes en número de la fecha de la clase procedente de la tupla Nacimientos "FNacimiento".
    
     * **dict_filtra_nacimientos_tipocentro_mes (datos, tipocentro, mes)**: Dada una lista de  tuplas de tipo Nacimientos, el tipo de centro y el mes en nombre, aportados como parámetros, devuelve un diccionario con una cadena de caracteres con el tipo de centro y el mes como clave y la lista de nacimientos producidos en dicho tipo de centro y dicho mes como valores.

#### Entrega 3

 * **Bloque 3**
 	
    * **dict_cuenta_numero_nacimientos_por_hospital (datos)**: Dada una lista de  tuplas de tipo Nacimientos, facilitada como parámetro, devuelve un diccionario con una cadena de caracteres con el nombre del hospital en cuestión, como clave, y el número total de nacimientos producidos en dicho hospital como valor..
    * **dict_calcula_altura_promedio_por_hospital (datos)**: Dada una lista de  tuplas de tipo Nacimientos, facilitada como parámetro, devuelve un diccionario con una cadena de caracteres con el nombre del hospital en cuestión, como clave, y el promedio de altura de los nacimientos para dicho hospital, como valor.	

    * **dict_calcula_porcentaje_nacimientos_por_género_provincia(datos)**: Dada una lista de  tuplas de tipo Nacimientos, facilitada como parámetro, devuelve un diccionario con una cadena de caracteres con la provincia del hospital en cuestión, como clave, y el porcentaje de hombres y mujeres respecto del total de nacimientos, producidos en dicha provincia como valor.
    
    * **dict_calcula_nacimientos_menor_peso_por_municipio(datos)**:  Dada una lista de  tuplas de tipo Nacimientos, facilitada como parámetro, devuelve un diccionario con una cadena de caracteres con el municipio del hospital en cuestión, como clave, y una lista con los pesos de los nacimientos producidos en dicho municipio, ordenada de menor a mayor, como valor. 

 
 * **Bloque 4 (Voluntario)**
 	
    * **convierte_mesnum_mesnom(mes)**: Función auxiliar que convierte el mes en número aportado como parámetro a mes como nombre, para hacer uso del diccionario siguiente como objeto de estudio en la gráfica a continuación.

    * **dict_nacimientos_por_mes(datos)**: Dada una lista de  tuplas de tipo Nacimientos, facilitada como parámetro, devuelve un diccionario con una cadena de caracteres con el mes de los nacimientos en cuestión, como clave, y el total de los nacimientos producidos en dicho mes, como valor.

    * **grafica_nacimientos_por_mes(etiquetas, valores, titulo, etiqueta_eje_x,etiqueta_eje_y)**: Dadas unas etiquetas, que corresponden a una lista de valores (eje x) para cada uno de los gráficos de barras, unos valores (eje y), que corresponden a las imágenes de cada uno de los gráficos, un título que defina los datos que se están observando en la gráfica de barras, así como las correspondientes etiquetas para cada uno de los ejes, todo ello aportado mediante parámetros, muestra una gráfica en la que se representan el total de nacimientos producidos en cada mes.


### Módulo test_nacimientos

En este módulo se han definido las siguientes funciones, las cuales son usadas para probar la función cuyo nombre posee. Por ejemplo, la función **test_lee_registros** prueba la función **lee_registros**.

* **test_lee_registros()**
* ** registros**: variable que recoge la lista formada por cada tupla de tipo Nacimientos leída mediante la función "test_lee_registros" para su posterior uso en los demás tests.
* **test_filtra_nacimientos_provincias() **
* **test_calcula_pesopromedio_género_provincias()**
* **test_calcula_altura_max_género_tipocentro()**
* **test_filtra_recientes_nacimientos_género_provincias()**
* **test_dict_filtra_nacimientos_tipocentro_mes()**
* **test_dict_cuenta_numero_nacimientos_por_hospital()**
* **test_dict_calcula_altura_promedio_por_hospital()**
* **test_dict_calcula_porcentaje_nacimientos_por_género_provincia()**
* **test_dict_calcula_nacimientos_menor_peso_por_municipio()**
* **test_dict_nacimientos_por_mes()**
* **test_grafica_nacimientos_por_mes()**
