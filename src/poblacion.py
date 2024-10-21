from collections import namedtuple
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero: str) -> list[RegistroPoblacion]:
    res = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            res.append(tupla)
    return res


def calcula_paises(poblaciones):
    res = set()
    for paises in poblaciones:
        res.add(paises.pais)
    return sorted(res)

def filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> list[(int, int)]:
    res = []
    for e in poblaciones:
        if e.pais == nombre_o_codigo or e.codigo == nombre_o_codigo:
            tupla = (e.año, e.censo)
            res.append(tupla)
    return res

def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set) -> list[(str, int)]:
    res = []
    for e in poblaciones:
        if  e.año == anyo and e.pais == paises:
            nombre_pais = e.pais
            num_habitantes = e.censo
            tupla = (nombre_pais, num_habitantes)    
            res.append(tupla)
    return res
    