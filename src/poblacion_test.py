from poblacion import*

def test_lee_poblaciones(ruta_fichero: str) -> list[RegistroPoblacion]:
    print('Test de lee_poblaciones')
    print('Mostrando las 5 primeras:')
    print(lee_poblaciones(ruta_fichero)[:5])
    print('Mostrando las 5 ultimas:')
    print(lee_poblaciones(ruta_fichero)[-5:])
    print("===============================================================")


def test_calcula_paises(poblaciones):
    print('Test de calcula_paises')
    print(calcula_paises(poblaciones))
    print("===============================================================")
    
def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print('Test de filtra_por_pais')
    print(filtra_por_pais(poblaciones, nombre_o_codigo))
    print("===============================================================")
    
def test_filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set) -> list[(str, int)]:
    print("Test filtra por pais y anyo")
    print(filtra_por_paises_y_anyo(poblaciones, anyo, paises))
    print("===============================================================")

    
    
    
    
    
    
    
    
    
    
    



if __name__ == '__main__':
    poblaciones = lee_poblaciones('data\population.csv')
    paises = set("Arab World", "Canada", "Germany")
    #test_lee_poblaciones('data\population.csv')
    #test_calcula_paises(poblaciones)
    #test_filtra_por_pais(poblaciones, "ARB")
    test_filtra_por_paises_y_anyo(poblaciones, 1989, paises)