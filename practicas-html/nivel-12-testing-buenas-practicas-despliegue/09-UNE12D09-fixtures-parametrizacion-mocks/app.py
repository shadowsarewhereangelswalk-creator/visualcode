import json
import sys
from datetime import datetime

PRACTICA = "UNE12D09"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D09"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from notificaciones import ClienteCorreo, enviar_recordatorio

resultado = enviar_recordatorio(
    {"correo": "karen@example.com", "activo": True},
    ClienteCorreo(),
    datetime(2027, 6, 9),
)
print(json.dumps(resultado, ensure_ascii=False, indent=2))
