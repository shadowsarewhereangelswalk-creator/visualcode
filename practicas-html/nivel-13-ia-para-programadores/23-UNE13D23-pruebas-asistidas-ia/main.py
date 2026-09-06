def crear_casos(especificacion):
    return [{"entrada":valor,"esperado":especificacion(valor)} for valor in ["","hola","ERROR urgente","consulta"]]
def especificacion(texto):
    if not texto: return "vacío"
    if "error" in texto.lower(): return "incidente"
    return "mensaje"
for caso in crear_casos(especificacion): print(caso)
