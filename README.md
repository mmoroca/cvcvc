# cvcvc_random.py

Script en Python que analiza un diccionario de palabras en español y selecciona aleatoriamente una palabra de 5 letras para cada patrón posible de consonantes (C) y vocales (V).

## ¿Qué hace?

1. Lee un archivo de texto con palabras en español (`dicc.txt`).
2. Filtra únicamente las palabras de exactamente 5 letras.
3. Clasifica cada palabra según su patrón consonante/vocal (ej: `cvcvc`, `vccvc`…).
4. Para cada patrón encontrado, selecciona una palabra al azar.
5. Muestra los resultados ordenados por patrón.

### Ejemplo de salida

```
PATRÓN  | PALABRA ALEATORIA
-------------------------
cccvc   | trans
cvccc   | parts
cvcvc   | papel
vccvc   | arbol
vcvcv   | aside
...
```

## Requisitos

- Python 3.x
- Un archivo `dicc.txt` con palabras en español, una por línea (codificación UTF-8).

No se necesitan librerías externas; el script usa únicamente módulos de la biblioteca estándar (`unicodedata`, `random`).

## Uso

```bash
python cvcvc_random.py
```

El archivo `dicc.txt` debe estar en el mismo directorio que el script. Si no se encuentra, se mostrará un mensaje de error.

## Estructura del código

| Función / Bloque | Descripción |
|---|---|
| `limpiar_tildes(texto)` | Elimina tildes y diacríticos usando normalización Unicode NFD. |
| `procesar_rae_random(ruta_archivo)` | Lógica principal: lee el diccionario, clasifica por patrón y elige una palabra aleatoria por patrón. |
| Bloque de ejecución | Llama a la función y muestra los resultados formateados por consola. |

## Notas

- Las palabras con tildes se normalizan antes de clasificar (ej: `árbol` → `arbol`) para que el patrón sea correcto.
- La selección aleatoria varía en cada ejecución del script.
- Solo se consideran palabras compuestas únicamente por letras del alfabeto (`isalpha()`), descartando números, guiones o símbolos.
