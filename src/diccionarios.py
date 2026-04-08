# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """

    # TU CÓDIGO AQUÍ
    frecuencia = {}
    
    for palabra in texto.lower().split():
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia
    pass


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
    """
    # TU CÓDIGO AQUÍ
    return {valor: clave for clave, valor in d.items()}
    pass


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    # TU CÓDIGO AQUÍ
    return {**d1, **d2}
    pass


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    # TU CÓDIGO AQUÍ
    return {clave: valor for clave, valor in d.items() if valor >= minimo}
    pass
