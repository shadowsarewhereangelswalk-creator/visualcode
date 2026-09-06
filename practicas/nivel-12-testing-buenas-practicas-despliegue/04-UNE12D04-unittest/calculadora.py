def sumar(a, b):
    return a + b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def promedio(valores):
    if not valores:
        raise ValueError("Se requiere al menos un valor")
    return sum(valores) / len(valores)
