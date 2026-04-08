# ============================================================
# MÓDULO 5: Loops
# ============================================================


import math


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    # TU CÓDIGO AQUÍ
    return list(range(1, n + 1))
    pass


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    # TU CÓDIGO AQUÍ
    multiplos = []
    for i in range(1, 11):
        multiplos.append(n * i)
    
    return multiplos
    pass


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    # TU CÓDIGO AQUÍ
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma
    pass


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    # TU CÓDIGO AQUÍ
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False    
    return True
    pass


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    # TU CÓDIGO AQUÍ
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    serie = [0, 1]

    while len(serie) < n:
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)
    return serie

    pass
