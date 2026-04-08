# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """

    # TU CÓDIGO AQUÍ
    total = 0
    for n in numeros:
        total += n
    return total
    pass


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """

    # TU CÓDIGO AQUÍ
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares
    pass


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    # TU CÓDIGO AQUÍ
    return list(reversed(lista))
    pass


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    # TU CÓDIGO AQUÍ
    nueva_lista = []
    vistos = set()
    for elemento in lista:
        if elemento not in vistos:
            nueva_lista.append(elemento)
            vistos.add(elemento)
    return nueva_lista
    pass


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    # TU CÓDIGO AQUÍ
    plana = []
    for sublista in lista:
        for elemento in sublista:
            plana.append(elemento)
    return plana
    pass
