import json
import os
from copy import deepcopy
print(os.getcwd())

def cargar_menu():
    '''
    Muestra un menú de opciones al usuario y espera a 
    que el usuario ingrese una opción.

    Retorna:
    str: La opción ingresada por el usuario.
    '''

    menu = input('''\nMenú de Opciones:
    1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los 
servicios.
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
7) Salir.
\n''')

    return menu

def validar_entero(entero: str):
    """ Verifica que el str ingresado sea un valor numérico, 
    devolviendo así un bool que indique con 
    'True' si se pudo llevar a cabo la validación."""
    flag = False

    if entero.isdigit():
        flag = True

    return flag

def validar_opciones():
    """Verifica que el str ingresado sea de caracter 
    numérico dando paso a la instancia de opciones las 
    cuales ejecutaran sus respectivas funciones"""

    opciones = cargar_menu()
    flag_validada = validar_entero(opciones)

    if flag_validada == True:
        opciones = int(opciones)
        if opciones > 7:
            print("Error. Ingrese un número acorde a las opciones.. ")
    else:
        print("Error. Ingrese un número acorde a las opciones.. ")

    return opciones

#FUNCIONES POR OPCIONES

def leer_json(nombre:str,extension:str,nombre_lista:str):
    '''
    Lee un archivo JSON y devuelve una lista específica 
    dentro del archivo.

    Parámetros:
    nombre (str): El nombre del archivo JSON sin la extensión.
    extension (str): La extensión del archivo (por ejemplo, 
    "json").
    nombre_lista (str): El nombre de la lista dentro del archivo 
    JSON que se desea obtener.

    Retorna: 
    list: La lista especificada dentro del archivo JSON, 
    si se encuentra.
    False: Si el archivo no se encuentra.
    '''
    try:
        with open(f"{nombre}.{extension}",'r') as archivo:
            data = json.load(archivo)
            lista = data

        return lista
    except FileNotFoundError:
        return False

lista = leer_json("./data","json","data_servicios")

def hallar_ancho_columna(lista:list,clave:str):
    '''
    Calcula el ancho máximo de una columna específica 
    en una lista de diccionarios.

    Parámetros:
    lista (list): Lista de diccionarios que contienen 
    los datos.
    clave (str): Clave de los diccionarios para la cual 
    se desea calcular el ancho máximo de la columna.

    Retorna:
    int: El ancho máximo de la columna correspondiente 
    a la clave especificada.
    '''
    
    ancho_max = 0
    for dicc in lista:
        ancho_max = max(ancho_max,len(dicc[clave]))

    return ancho_max

def rellenar_espacios(lista:list,lista_datos:list):
    '''
    Rellena con espacios en blanco los valores de las 
    columnas especificadas para que todos tengan el mismo ancho.

    Parámetros:
    lista (list): Lista de diccionarios que contienen los datos.
    lista_datos (list): Lista de claves de los diccionarios 
    cuyas columnas deben ser rellenadas.

    Retorna:
    list: La lista de diccionarios con los valores de las 
    columnas especificadas rellenados con espacios en blanco.
    '''
    for dato in lista_datos:
        ancho = hallar_ancho_columna(lista,dato)
        for dicc in lista:
            if len(dicc[dato]) < ancho:
                dicc[dato] = dicc[dato].ljust(ancho)

    return lista

def listar_datos(lista:list,lista_datos:list):
    '''
    Genera un mensaje que muestra los valores de 
    las claves especificadas en una lista de diccionarios, 
    formateados como una tabla.

    Parámetros:
    lista (list): Lista de diccionarios que contienen 
    los datos.
    lista_datos (list): Lista de claves de los diccionarios 
    cuyos valores se desean listar.

    Retorna:
    str: Un mensaje formateado que muestra los valores de las 
    claves especificadas en una tabla.

    '''
    msj = ""
    copia_lista = deepcopy(lista)
    nueva_lista = rellenar_espacios(copia_lista,lista_datos)

    for dicc in nueva_lista:
        for dato in lista_datos:
            msj += dicc[f"{dato}"] + " |"
        msj += "\n"
    
    return msj

'''
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.

4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.'''



# def asignar_totales(lista:list,clave_1:str, clave_2:str):

#     for i in range(len(lista)):
#         primer_valor= lista[i].get(clave_1)
#         segundo_valor= lista[i].get(clave_2)
#         valor_asginar = lambda cantidad, preciounitario: cantidad * preciounitario\
#         (primer_valor,segundo_valor)

#         lista[i].update({"totalServicio":valor_asginar})

#     return lista

# lista = asignar_totales(lista,"cantidad","precioUnitario")
# print(listar_datos(listar_datos,["id_servicio",
#     "descripcion",
#     "tipo",
#     "precioUnitario",
#     "cantidad",
# "totalServicio"]))

def guardar_archivo(nombre_extension:str,contenido:str):
    '''

    Guarda contenido en un archivo especificado.
    Parámetros:
    nombre_extension (str): El nombre del archivo con su 
    extensión (por ejemplo, "archivo.txt").
    contenido (str): El contenido que se desea escribir 
    en el archivo.
    Retorna:
    bool: True si el archivo se creó y escribió correctamente, 
    False si hubo un error durante el proceso.

    '''
    try:
        with open(nombre_extension,'w') as archivo:
            archivo.write(contenido)
        
        print(f"Se creó el archivo: {nombre_extension}")

        return True
    except Exception as e:
        print(f"Error al crear el archivo: {nombre_extension}")
        print(e)
        return False

def hallar_coincidentes(lista:list,clave:str,comparador:str):
    '''
    Encuentra los elementos en una lista de diccionarios 
    cuyo valor asociado a una clave es igual al comparador dado.

    Parámetros:
    lista (list): Lista de diccionarios que se desea buscar.
    clave (str): Clave para la cual se busca el valor coincidente.
    comparador (str): Valor que se desea comparar con los valores 
    asociados a la clave.

    Retorna:
    list: Lista de diccionarios que contienen los elementos cuyo 
    valor asociado a la clave es igual al comparador.

    '''
    coincidentes = []

    for dicc in lista:
        valor_dicc = dicc.get(clave)
        if valor_dicc == comparador:
            coincidentes.append(dicc)

    return coincidentes

def ordenar_valores(lista:list,clave:str):
    '''Ordena una lista de diccionarios en 
    función de una clave específica.
    Parámetros:
    lista (list): Lista de diccionarios que 
    se desea ordenar.
    clave (str): Clave por la cual se desea 
    ordenar la lista de diccionarios.
    Retorna:
    list: Una nueva lista de diccionarios ordenada 
    por el valor de la clave especificada.
'''
    return sorted(lista, key=lambda x: x[clave])



