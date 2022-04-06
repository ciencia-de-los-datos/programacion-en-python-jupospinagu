"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
with open("data.csv", "r") as file:
 data = file.readlines()
 data = [line.replace("\n", "") for line in data]
 data = [line.split("\t") for line in data]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data_columna2 = [fila[1] for fila in data]
    data_columna2= [
    [int(field) if i_row >= 0 else field for field in row]
    for i_row, row in enumerate(data_columna2)]
    x = sum([row[0] for row in data_columna2])

    return x
    

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data_columna1 = [fila[0] for fila in data]

    
    Diccionario = dict(
    [
        ("A", data_columna1.count('A')),
        ("B", data_columna1.count('B')),
        ("C", data_columna1.count('C')),
        ("D", data_columna1.count('D')),
        ("E", data_columna1.count('E')),
    ]
)
    y= sorted(list(Diccionario.items()))

    return y


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import itertools
    from operator import itemgetter
    
    data_punto3 = [ [row[0]] + [int(row[1])] for row in data ]
    data_punto3.sort()
    data_punto3

    data_grouped_by_letra = {
    letra: list(group)
    for letra, group in itertools.groupby(
        data_punto3[0:],
        key=itemgetter(0),
    )
}
    sum_punto3 = [
    [
        letra,
        sum([row[1] for row in data_grouped_by_letra[letra]]),
    ]
    for letra in data_grouped_by_letra.keys()
]
    y = dict(sum_punto3)
    y = sorted(list(y.items()))
    return y
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import itertools
    from operator import itemgetter

    with open("data.csv", "r") as file:
     data_prueba = file.readlines()
     data_prueba = [line.replace("\n", "") for line in data_prueba]
     data_prueba = [line.split("-") for line in data_prueba]

    data_punto4 = [ [(row[1])]  for row in data_prueba ]
    data_punto4.sort()
    data_punto4[0:5]

    data_grouped_by_month = {
    mes: list(group)
    for mes, group in itertools.groupby(
        data_punto4[0:],
        key=itemgetter(0),
    )
}
    contador_mes = [
    [
        mes,
        len([row[0] for row in data_grouped_by_month[mes]]),
    ]
    for mes in data_grouped_by_month.keys()
]
    z = dict(contador_mes)
    z = sorted(list(z.items()))
    return z
    


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data_punto5 = [ [(row[0]), (int(row[1]))]  for row in data ]
    data_punto5.sort()
    data_punto5[0:5]

    import itertools
    from operator import itemgetter

    data_grouped_by_letra = {
    letra: list(group)
    for letra, group in itertools.groupby(
        data_punto5[0:],
        key=itemgetter(0),
    )
}
    resultado_punto5 = [
    [
        letra,
        (max([row[1] for row in data_grouped_by_letra[letra]])),
        (min([row[1] for row in data_grouped_by_letra[letra]]))
    ]
    for letra in data_grouped_by_letra.keys()
]

    resultado_punto5 = [ tuple(x) for x in resultado_punto5 ]
    
    return resultado_punto5
    


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import itertools
    from operator import itemgetter
    
    data_punto6 = [ (row[4])  for row in data ]
    data_punto6 = [line.split(",") for line in data_punto6]
    data_punto6[0:5]

    flat_list = []


    for item in data_punto6:
        flat_list += item

    flat_list = [line.split(":") for line in flat_list]
    flat_list = sorted(flat_list, key=itemgetter(0), reverse=False)
    flat_list = [ [row[0]]  + [int(row[1])]  for row in flat_list ]
    flat_list[0:5]

    

    data_grouped_by_letras = {
    letras: list(group)
    for letras, group in itertools.groupby(
        flat_list[0:],
        key=itemgetter(0),
    )
}
    resultado_punto6 = [
    [
        letras,
        (min([row[1] for row in data_grouped_by_letras[letras]])),
        (max([row[1] for row in data_grouped_by_letras[letras]]))
    ]
    for letras in data_grouped_by_letras.keys()
]
    resultado_punto6 = [ tuple(x) for x in resultado_punto6 ]

    return resultado_punto6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
