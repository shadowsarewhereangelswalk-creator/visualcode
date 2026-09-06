import json
from pathlib import Path


class GestorTareas:
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def listar(self):
        if not self.ruta.exists():
            return []
        return json.loads(self.ruta.read_text(encoding="utf-8"))

    def crear(self, titulo, prioridad="media"):
        titulo = titulo.strip()
        if len(titulo) < 3 or prioridad not in {"baja", "media", "alta"}:
            raise ValueError("Tarea no válida")
        tareas = self.listar()
        tarea = {
            "id": max((item["id"] for item in tareas), default=0) + 1,
            "titulo": titulo,
            "prioridad": prioridad,
            "completada": False,
        }
        tareas.append(tarea)
        self._guardar(tareas)
        return tarea

    def completar(self, tarea_id):
        tareas = self.listar()
        for tarea in tareas:
            if tarea["id"] == tarea_id:
                tarea["completada"] = True
                self._guardar(tareas)
                return tarea
        raise LookupError("Tarea no encontrada")

    def eliminar(self, tarea_id):
        tareas = self.listar()
        nuevas = [tarea for tarea in tareas if tarea["id"] != tarea_id]
        if len(nuevas) == len(tareas):
            raise LookupError("Tarea no encontrada")
        self._guardar(nuevas)

    def _guardar(self, tareas):
        self.ruta.write_text(
            json.dumps(tareas, ensure_ascii=False, indent=2), encoding="utf-8"
        )
