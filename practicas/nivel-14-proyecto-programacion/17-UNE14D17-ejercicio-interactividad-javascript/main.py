from pathlib import Path
js='''function validarCorreo(correo){return /^[^@\\s]+@[^@\\s]+\\.[A-Za-z]{2,}$/.test(correo)}function validarMensaje(mensaje){return mensaje.trim().length>=10}console.log(validarCorreo("karen@ejemplo.com"),validarMensaje("Mensaje de prueba"));'''
Path("validaciones.js").write_text(js,encoding="utf-8")
print("validaciones.js creado")
