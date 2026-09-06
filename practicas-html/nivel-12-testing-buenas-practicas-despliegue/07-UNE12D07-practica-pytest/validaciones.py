import re


def validar_usuario(nombre, correo, edad):
    errores = []
    if len(nombre.strip()) < 3:
        errores.append("nombre")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
        errores.append("correo")
    if not 18 <= edad <= 120:
        errores.append("edad")
    return {"valido": not errores, "errores": errores}


def calcular_progreso(completadas, total):
    if total <= 0 or not 0 <= completadas <= total:
        raise ValueError("Progreso no válido")
    return completadas / total * 100
