import math


def pagina_valida(pagina, por_pagina, maximo=100):
    return isinstance(pagina, int) and isinstance(por_pagina, int) and pagina >= 1 and 1 <= por_pagina <= maximo


def crear_respuesta(datos, total, pagina=1, por_pagina=20):
    total_paginas = math.ceil(total / por_pagina) if total else 0
    return {
        "datos": datos,
        "meta": {"total": total, "pagina": pagina, "por_pagina": por_pagina, "total_paginas": total_paginas},
    }


def crear_error(codigo, mensaje, detalles=None):
    error = {"codigo": str(codigo), "mensaje": str(mensaje)}
    if detalles is not None:
        error["detalles"] = detalles
    return {"error": error}
