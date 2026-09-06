import sys


def construir_perfil(argumentos):
    nombre = argumentos[0].strip().title() if argumentos else "Karen"
    especialidad = argumentos[1].strip().title() if len(argumentos) > 1 else "Inteligencia Artificial"
    horas = int(argumentos[2]) if len(argumentos) > 2 else 6
    return {
        "nombre": nombre,
        "especialidad": especialidad,
        "horas_semanales": horas,
    }


def crear_mensajes(perfil):
    return [
        f'Hola, {perfil["nombre"]}.',
        f'Ruta activa: {perfil["especialidad"]}.',
        f'Meta semanal: {perfil["horas_semanales"]} horas de práctica.',
    ]


def main():
    perfil = construir_perfil(sys.argv[1:])
    for mensaje in crear_mensajes(perfil):
        print(mensaje)


if __name__ == "__main__":
    main()
