import json
def clasificar_mensaje(texto):
    limpio=" ".join(texto.strip().split()); t=limpio.lower()
    if any(p in t for p in ("comprar","precio","cotización")): categoria="ventas"
    elif any(p in t for p in ("error","no funciona","problema")): categoria="soporte"
    else: categoria="general"
    return {"mensaje":limpio,"categoria":categoria,"requiere_humano":categoria=="soporte"}
print(json.dumps(clasificar_mensaje("Mi cuenta no funciona"),ensure_ascii=False,indent=2))
