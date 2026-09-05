def normalizar(registros):
    return {registro.strip().lower() for registro in registros if registro.strip()}


def comparar_clientes(lista_a, lista_b):
    clientes_a = normalizar(lista_a)
    clientes_b = normalizar(lista_b)
    return {
        "coincidencias": clientes_a & clientes_b,
        "solo_a": clientes_a - clientes_b,
        "solo_b": clientes_b - clientes_a,
        "todos": clientes_a | clientes_b,
        "diferencias": clientes_a ^ clientes_b,
    }


def mostrar_grupo(nombre, valores):
    contenido = ", ".join(sorted(valor.title() for valor in valores)) or "Ninguno"
    print(f"{nombre}: {contenido}")


def main():
    campaña_email = ["Ana", "Luis", "Marta", "Ana", "Diego"]
    campaña_redes = ["Marta", "Sofía", "Luis", "Pedro", "Sofía"]
    comparacion = comparar_clientes(campaña_email, campaña_redes)

    mostrar_grupo("Coincidencias", comparacion["coincidencias"])
    mostrar_grupo("Solo correo", comparacion["solo_a"])
    mostrar_grupo("Solo redes", comparacion["solo_b"])
    mostrar_grupo("Todos", comparacion["todos"])
    mostrar_grupo("Alcance exclusivo", comparacion["diferencias"])


if __name__ == "__main__":
    main()
