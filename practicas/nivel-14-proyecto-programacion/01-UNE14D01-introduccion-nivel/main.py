import json
proyecto={"nombre":"Asistente de solicitudes","frontend":"HTML5/CSS3/JavaScript","backend":"Python","base_datos":"SQLite","ia":"Clasificación de mensajes","estado":"inicio"}
print(json.dumps(proyecto,ensure_ascii=False,indent=2))
