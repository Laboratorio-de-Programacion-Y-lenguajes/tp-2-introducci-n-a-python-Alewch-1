# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    # TU CÓDIGO AQUÍ
    return [func(elemento) for elemento in lista]
    pass


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    # TU CÓDIGO AQUÍ
    return lambda x: f(g(x))
    pass


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}
    # TU CÓDIGO AQUÍ
    def wrapper(*argum):
        # Usamos los argumentos como clave (tupla inmutable)
        key = argum
        if key not in cache:
            cache[key] = func(*argum)
        return cache[key]
    
    return wrapper
    pass


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    # TU CÓDIGO AQUÍ
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
    pass
