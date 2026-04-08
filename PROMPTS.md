# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Cloude

**Prompt usado**: Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    eficiente y robusto
> 

**Resultado obtenido**:
if not isinstance(valor, str):
        raise TypeError(f"Se esperaba un string, se recibió: {type(valor).__name__}")

    valor_limpio = valor.strip()

    if not valor_limpio:
        raise ValueError("El string está vacío o contiene solo espacios.")

    try:
        return float(valor_limpio)
    except ValueError:
        raise ValueError(f"No se puede convertir '{valor_limpio}' a float.")


**¿Lo usaste tal cual o lo modificaste?** Lo modifique para que lo haga robusto y eficiente.


---

### 2 - condicionales.py

**Herramienta**: Cloude y se probo el mismo prompt con gemini, deepseek y gpt

**Prompt usado**:
Requiero de una funcion que evalua notas de parciales en lenguaje python que siga las siguientes consignas, retorna una categoria tipo String y recibe como parametro una nota tipo float. Si la nota es mayor o igual a 9 retorna Sobresaliente, si es mayor o igual a 7 retorna Bueno, si es mayor o igual a 6 retorna Aprobado, si es menos a 6 retorna Desaprobado. Que sea eficiente y respete buenas practicas.
> 

**Resultado obtenido**: Obtuve buen resultado con una modificacion al final que me saco un if menos y ademas no utilizo el if encadenado ya que la evaluacion se detiene apenas retorne un valor, este resultado tal vez fue gracias al "eficiente", ya que probe con otras IAs y me pusieron if encadenados(tiene su pro y su contra ya que le saca un poco de semantica al bloque). Tambien me mostro otra opcion pero mas robusto. 
def evaluar_nota(nota: float) -> str:
 if nota >= 9:
        return "Sobresaliente"
    if nota >= 7:
        return "Bueno"
    if nota >= 6:
        return "Aprobado"
    return "Desaprobado"




**¿Lo usaste tal cual o lo modificaste?** Lo modifique para darle un poco de contexto, le dije el lenguaje, que tipo de dato de entrada y salida deberia tener y que propiedades deberia tener y respetar.


---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
