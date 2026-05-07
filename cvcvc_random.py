import unicodedata
import random # Necesitamos esta librería

def limpiar_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                  if unicodedata.category(c) != 'Mn')

def procesar_rae_random(ruta_archivo):
    vocales = set("aeiou")
    # Ahora usamos una lista para guardar todas las palabras de cada patrón
    diccionario_de_listas = {}

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                palabra = linea.strip().lower()
                
                if len(palabra) == 5 and palabra.isalpha():
                    palabra_limpia = limpiar_tildes(palabra)
                    patron = "".join(['v' if c in vocales else 'c' for c in palabra_limpia])
                    
                    # Si el patrón no existe, creamos una lista vacía
                    if patron not in diccionario_de_listas:
                        diccionario_de_listas[patron] = []
                    
                    # Añadimos la palabra a la lista de ese patrón
                    diccionario_de_listas[patron].append(palabra)
        
        # Ahora elegimos una al azar para cada patrón
        resultados_random = {}
        for patron, lista_palabras in diccionario_de_listas.items():
            resultados_random[patron] = random.choice(lista_palabras)
            
        return resultados_random

    except FileNotFoundError:
        return "No se encuentra el archivo dicc.txt"

# Ejecución
resultados = procesar_rae_random("dicc.txt")

# Mostrar resultados
print(f"{'PATRÓN':<7} | {'PALABRA ALEATORIA'}")
print("-" * 25)
for p in sorted(resultados.keys()):
    print(f"{p:<7} | {resultados[p]}")