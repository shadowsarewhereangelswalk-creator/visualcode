def dentro_alcance(funcion):
    permitidas={"crear solicitud","listar solicitudes","clasificar mensaje","editar estado"}
    return funcion.lower() in permitidas
for funcion in ["Crear solicitud","Procesar pagos","Clasificar mensaje"]:
    print(funcion,dentro_alcance(funcion))
