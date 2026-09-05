DIAS = ("lunes", "martes", "miércoles", "jueves", "viernes")


def crear_sesion(dia, hora, tema, duracion):
    if dia.lower() not in DIAS:
        raise ValueError("El día debe ser laborable")
    if duracion <= 0:
        raise ValueError("La duración debe ser positiva")
    return dia.lower(), hora, tema.strip(), int(duracion)


def calcular_fin(sesion):
    dia, hora, tema, duracion = sesion
    horas, minutos = map(int, hora.split(":"))
    total_minutos = horas * 60 + minutos + duracion
    return dia, f"{total_minutos // 60:02d}:{total_minutos % 60:02d}", tema


def ordenar_agenda(sesiones):
    indice_dias = {dia: posicion for posicion, dia in enumerate(DIAS)}
    return tuple(sorted(sesiones, key=lambda sesion: (indice_dias[sesion[0]], sesion[1])))


def main():
    sesiones = (
        crear_sesion("lunes", "09:30", "Python básico", 90),
        crear_sesion("miércoles", "14:00", "Colecciones", 60),
        crear_sesion("martes", "11:15", "Cadenas", 75),
    )
    for sesion in ordenar_agenda(sesiones):
        dia, fin, tema = calcular_fin(sesion)
        print(f"{dia.title()} · {tema} · termina a las {fin}")


if __name__ == "__main__":
    main()
