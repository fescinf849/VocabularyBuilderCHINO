import csv

# Ejecutar como: python3 csv2html.py > salida.html


# Nombre del archivo CSV de entrada
archivo_csv = "e01s05.csv"

# Leemos el CSV y generamos el HTML
html_salida = []

with open(archivo_csv, encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        if len(fila) != 3:
            continue  # Saltar líneas incorrectas

        chino, pinyin, traduccion = fila

        bloque = (
            f'<div class="word_or_phrase">'
            f'<span class="pinyin"> {pinyin} </span>'
            f'<span class="chino">{chino}</span>'
            f'<span class="trad">{traduccion}</span>'
            f'</div>'
        )

        html_salida.append(bloque)

# Imprimir el resultado HTML
print("\n".join(html_salida))
