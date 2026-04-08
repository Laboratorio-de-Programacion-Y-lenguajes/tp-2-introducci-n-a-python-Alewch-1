# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    # TU CÓDIGO AQUÍ
    texto_limpio = texto.lower().replace(" ", "")

    texto_invertido = ""
    for caracter in texto_limpio:
        texto_invertido = caracter + texto_invertido
    
    return texto_limpio == texto_invertido
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    # TU CÓDIGO AQUÍ
    palabras = texto.split()
    resultado = []
    
    for p in palabras:    
        resultado.append(p.capitalize())
    
    return " ".join(resultado)
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    # TU CÓDIGO AQUÍ
    vocales = "aeiou"
    contador = 0
    
    texto_min = texto.lower()
    
    for letra in texto_min:
        if letra in vocales:
            contador = contador + 1

    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    # TU CÓDIGO AQUÍ
    abc_minus = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    
    for letra in texto:
        if letra in abc_minus:
            posicion = abc_minus.find(letra)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado = resultado + abc_minus[nueva_posicion]
        elif letra in abc_mayus:
            posicion = abc_mayus.find(letra)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado = resultado + abc_mayus[nueva_posicion]
        else:
            resultado = resultado + letra
    
    return resultado
    pass
