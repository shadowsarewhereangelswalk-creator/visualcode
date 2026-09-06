def organizar_tareas(tareas):
    tareas = list(tareas)
    tareas.append("Publicar proyecto")
    tareas.insert(1, "Validar requisitos")
    tareas.extend(["Crear respaldo", "Enviar informe"])
    tareas.remove("Crear respaldo")
    completada = tareas.pop(0)
    tareas.sort(key=str.casefold)
    return completada, tareas


def crear_prioridades(tareas):
    return [
        {"posicion": indice, "tarea": tarea, "urgente": "Validar" in tarea}
        for indice, tarea in enumerate(tareas, start=1)
    ]


def main():
    iniciales = ["Diseñar interfaz", "Programar funciones", "Probar aplicación"]
    completada, pendientes = organizar_tareas(iniciales)
    prioridades = crear_prioridades(pendientes)

    print(f"Tarea completada: {completada}")
    print("Tareas pendientes:")
    for item in prioridades:
        estado = "urgente" if item["urgente"] else "normal"
        print(f'{item["posicion"]}. {item["tarea"]} · {estado}')


if __name__ == "__main__":
    main()
