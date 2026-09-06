orden={"alta":0,"media":1,"baja":2}
requerimientos=[("Validar entradas","alta"),("Exportar CSV","baja"),("Crear solicitud","alta"),("Clasificar mensaje","media")]
for nombre,prioridad in sorted(requerimientos,key=lambda item:orden[item[1]]): print(prioridad,nombre)
