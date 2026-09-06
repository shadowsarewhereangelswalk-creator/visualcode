from dataclasses import dataclass
@dataclass(frozen=True)
class Tarea:
    titulo:str
    prioridad:int
def ordenar_tareas(tareas):
    return sorted(tareas,key=lambda tarea:(-tarea.prioridad,tarea.titulo.lower()))
tareas=[Tarea("Documentar API",2),Tarea("Corregir error",3),Tarea("Crear prueba",2)]
for tarea in ordenar_tareas(tareas): print(tarea)
