entidades={"Usuario":{"pk":"id","campos":["nombre","correo"]},"Solicitud":{"pk":"id","fk":"usuario_id","campos":["mensaje","categoria","estado"]}}
relaciones=[("Usuario","1:N","Solicitud")]
print(entidades)
print(relaciones)
