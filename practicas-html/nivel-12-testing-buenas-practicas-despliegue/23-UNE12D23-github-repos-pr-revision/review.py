def validar_pull_request(datos):
    errores = []
    if len(datos.get("titulo", "").strip()) < 10:
        errores.append("titulo")
    if len(datos.get("descripcion", "").strip()) < 20:
        errores.append("descripcion")
    if not datos.get("pruebas_aprobadas", False):
        errores.append("pruebas")
    if not datos.get("revisor", "").strip():
        errores.append("revisor")
    return {
        "aprobable": not errores,
        "errores": errores,
        "resumen": f"{datos.get('autor', 'Autor')} → {datos.get('rama_base', 'main')}",
    }
