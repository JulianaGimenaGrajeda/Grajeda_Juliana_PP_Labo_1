#FUNCIONES GENÉRICAS PARA EL PARCIAL

#importación de archivos
from archivo import *

#copias de listas/dicc
from copy import deepcopy

#limpiar pantalla
from os import system 
system("cls")


#ORDENAR LISTA CON DICCIONARIOS
def ordenar_valores(lista:list,clave:str):
    '''
    Ordena una copia de la lista de diccionarios 
    en función de una clave específica.

    Parámetros:
    lista (list): Lista de diccionarios que se 
    desea ordenar.
    clave (str): Clave por la cual se desea ordenar 
    la lista de diccionarios.

    Retorna:
    list: Una nueva lista de diccionarios ordenada 
    por el valor de la clave especificada.
    '''
    copia_lista = deepcopy(lista)
    return sorted(copia_lista, key=lambda x: x[clave])

#ORDENAR ELEMENTOS DE UNA LISTA
def Ordenar_lista(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

#HALLAR MENOR/MAYOR VALOR(CAMBIAR SIGNO) LISTA DICCIONARIO (VAN TODAS JUNTAS)
def es_numero(valor):
    '''
    Verifica si un valor dado puede convertirse 
    en un número de punto flotante.

    Parámetros:
    valor: El valor que se desea verificar.

    Retorna:
    bool: True si el valor puede convertirse 
    en un número de punto flotante, False en caso contrario.
    '''
    try:
        float(valor)
        return True
    except ValueError:
        return False

def castear_lista(lista: list) -> list:
    '''
    Convierte los valores numéricos en 
    una lista de diccionarios a tipo float.

    Parámetros:
    lista (list): Lista de diccionarios 
    cuyos valores numéricos se desean convertir.

    Retorna:
    list: La lista de diccionarios con los 
    valores numéricos convertidos a tipo float.
    '''
    for dicc in lista:
        for key in dicc:
            if es_numero(dicc[key]):
                dicc[key] = float(dicc[key])
    return lista

def hallar_menor_valor(lista:list,clave:str) -> list:
    '''
    Encuentra los elementos con el menor valor 
    asociado a una clave en una lista de diccionarios.

    Parámetros:
    lista (list): Lista de diccionarios que se desea buscar.
    clave (str): Clave para la cual se busca el menor valor.

    Retorna:
    list: Lista de diccionarios que contienen los 
    elementos con el menor valor asociado a la clave.

    '''
    copia_lista = deepcopy(lista)
    lista_casteada = castear_lista(copia_lista)
    lista_mostrar = deepcopy(lista)
    valor_min = lista_casteada[0][clave]
    lista_min = []

    for i in range(len(lista_casteada)):
        valor_dicc_falso = lista_casteada[i].get(clave)
        if  valor_dicc_falso < valor_min:
            valor_min = valor_dicc_falso
            lista_min = [lista_mostrar[i]]
        elif valor_dicc_falso == valor_min:
            lista_min.append(lista_mostrar[i])

    return lista_min

#HALLAR MENOR/MAYOR VALOR LISTA ¡¡¡¡DEVUELVE POSICIONES!!!
def buscar_mayor_menor_valor(lista:list,comparador:str) -> list:
    '''Busca el mayor valor dentro de 
    una lista de datos
    Parametros: Pide la lista de datos a utilizar
    Retorno: Devuelve una lista con las posiciones 
    del mayor valor encontrado'''

    mayor_valor = lista[0]
    posiciones = [0]

    if comparador == "mayor":
        for i in range(1,len(lista)):
            if lista[i] > mayor_valor:
                mayor_valor = lista[i]
                posiciones = [i]
            elif lista[i] == mayor_valor:
                posiciones.append(i)
    else:
        for i in range(1,len(lista)):
            if lista[i] < mayor_valor:
                mayor_valor = lista[i]
                posiciones = [i]
            elif lista[i] == mayor_valor:
                posiciones.append(i)

    return posiciones

#CALCULAR PROMEDIO LISTA
def calcular_promedio(lista:list,mensaje:str):
    '''Pide una lista para caclular el promedio de los
    datos dentro de la misma.
    Parametros: la lista con la que trabajaremos, mensaje
    para mostrar junto con el resultado de la operación'''
    acumulador = 0
    contador = 0

    for dato in lista:
        if type(dato) == float or type(dato) == int:
            acumulador += dato
            contador += 1

    if acumulador != 0:
        promedio = acumulador / contador
        print(mensaje + str(promedio))
        return promedio
    else:
        print("No se pudo calcular el promedio.. Revise la lista ingresada")

#CALCULAR PROMEDIO LISTA CON DICCIONARIO TODO JUNTO

def es_numero(valor):
    '''
    Verifica si un valor dado puede convertirse 
    en un número de punto flotante.

    Parámetros:
    valor: El valor que se desea verificar.

    Retorna:
    bool: True si el valor puede convertirse 
    en un número de punto flotante, False en caso contrario.
    '''
    try:
        float(valor)
        return True
    except ValueError:
        return False

def castear_lista(lista: list) -> list:
    '''
    Convierte los valores numéricos en 
    una lista de diccionarios a tipo float.

    Parámetros:
    lista (list): Lista de diccionarios 
    cuyos valores numéricos se desean convertir.

    Retorna:
    list: La lista de diccionarios con los 
    valores numéricos convertidos a tipo float.
    '''
    for dicc in lista:
        for key in dicc:
            if es_numero(dicc[key]):
                dicc[key] = float(dicc[key])
    return lista

def calcular_promedio(lista:list,clave:str):
    '''
    Calcula el promedio de los valores asociados 
    a una clave en una lista de diccionarios.

    Parámetros:
    lista (list): Lista de diccionarios que se desea calcular.
    clave (str): Clave para la cual se desea calcular 
    el promedio de los valores asociados.

    Retorna:
    float or str: El promedio de los valores asociados a 
    la clave si se puede calcular correctamente.
    Un mensaje de error si ocurre un problema durante el cálculo.
    '''
    copia_lista = deepcopy(lista)
    lista_casteada = castear_lista(copia_lista)
    contador = 0
    acumulador = 0

    for dicc in lista_casteada:
        acumulador += dicc[clave]
        contador += 1

    if contador != 0 and acumulador != 0:
        resultado = acumulador / contador
    else:
        resultado = "El calculo de promedio no pudo \
llevarse a cabo, a ocurrido un error.. "

    return resultado

#MENUS OPCIONALES
def cargar_menu():
    '''
    Muestra un menú de opciones al usuario y espera a 
    que el usuario ingrese una opción.

    Retorna:
    str: La opción ingresada por el usuario.
    '''

    menu = input('''\nMenú de Opciones:
    
\n''')

    return menu

#VALIDAR OPCIONES STR
def validar_str(caracter: str):
    '''
    Valida si un carácter o una cadena de
    caracteres contiene solo letras del alfabeto.
    Parámetros:
    caracter (str): El carácter o cadena de 
    caracteres a validar.
    Retorna:
    bool: True si el carácter o cadena de caracteres 
    contiene solo letras, False en caso contrario.
    '''
    
    flag = False

    if caracter.isalpha():
        flag = True

    return flag

def validar_opciones():
    '''
    Muestra un menú de opciones al usuario y 
    valida que la opción ingresada sea una letra.

    Retorna:
    str: La opción ingresada por el usuario en 
    mayúsculas si es válida, o muestra un mensaje de error.
    '''

    opciones = cargar_menu()
    flag_validada = validar_str(opciones)

    if flag_validada == True:
        opciones = opciones.upper()
    else:
        print("Error. Ingrese un caracter acorde a las opciones.. ")

    return opciones

#VALIDAR OPCIONES NUMEROS
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
    else:
        print("Error. Ingrese un número acorde a las opciones.. ")

    return opciones

#MENU FUNCIONES OPCIONES
while True:
    opciones = validar_opciones()

    match opciones:
        case '':
            pass
        case '':
            pass
        case '':
            pass
        case '':
            break