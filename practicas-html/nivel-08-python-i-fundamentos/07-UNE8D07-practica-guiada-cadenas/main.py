import re
import unicodedata


def normalizar_texto(texto):
    limpio = " ".join(texto.strip().split())
    return limpio[0].upper() + limpio[1:] if limpio else ""


def crear_slug(texto):
    base = unicodedata.normalize("NFKD", texto)
    base = "".join(caracter for caracter in base if not unicodedata.combining(caracter))
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def analizar_texto(texto):
    palabras = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", texto)
    letras = [caracter.lower() for caracter in texto if caracter.isalpha()]
    vocales = sum(caracter in "aeiouáéíóúü" for caracter in letras)
    return {
        "caracteres": len(texto),
        "palabras": len(palabras),
        "letras": len(letras),
        "vocales": vocales,
        "consonantes": len(letras) - vocales,
        "slug": crear_slug(texto),
    }


def generar_ficha(titulo, descripcion):
    titulo = normalizar_texto(titulo)
    descripcion = normalizar_texto(descripcion)
    analisis = analizar_texto(descripcion)
    lineas = [
        f"Título: {titulo}",
        f"Identificador: {crear_slug(titulo)}",
        f"Descripción: {descripcion}",
        f'Palabras: {analisis["palabras"]}',
        f'Vocales: {analisis["vocales"]}',
        f'Consonantes: {analisis["consonantes"]}',
    ]
    return "\n".join(lineas)


if __name__ == "__main__":
    print(generar_ficha("  asistente de ventas con IA ", " automatiza respuestas y organiza clientes "))
