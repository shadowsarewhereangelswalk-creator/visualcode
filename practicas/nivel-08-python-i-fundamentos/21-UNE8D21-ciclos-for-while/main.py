def procesar_comandos(comandos):
    tareas = []
    historial = []
    posicion = 0
    activo = True

    while activo and posicion < len(comandos):
        accion, valor = comandos[posicion]
        posicion += 1

        if accion == "agregar":
            tareas.append({"nombre": valor, "completada": False})
            historial.append(f"Agregada: {valor}")
        elif accion == "completar":
            for tarea in tareas:
                if tarea["nombre"] == valor:
                    tarea["completada"] = True
                    historial.append(f"Completada: {valor}")
                    break
            else:
                historial.append(f"No encontrada: {valor}")
        elif accion == "eliminar":
            tareas = [tarea for tarea in tareas if tarea["nombre"] != valor]
            historial.append(f"Eliminada: {valor}")
        elif accion == "salir":
            activo = False
            historial.append("Sesión finalizada")
        else:
            historial.append(f"Acción inválida: {accion}")

    return tareas, historial


def generar_reporte(tareas):
    lineas = []
    for indice, tarea in enumerate(tareas, start=1):
        estado = "completada" if tarea["completada"] else "pendiente"
        lineas.append(f'{indice}. {tarea["nombre"]} · {estado}')
    return lineas


def main():
    comandos = [
        ("agregar", "Diseñar solución"),
        ("agregar", "Programar funciones"),
        ("agregar", "Probar resultados"),
        ("completar", "Diseñar solución"),
        ("eliminar", "Probar resultados"),
        ("agregar", "Publicar proyecto"),
        ("salir", ""),
    ]
    tareas, historial = procesar_comandos(comandos)

    print("Historial:")
    for evento in historial:
        print(evento)
    print("Tareas:")
    for linea in generar_reporte(tareas):
        print(linea)


if __name__ == "__main__":
    main()
