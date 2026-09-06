import re
def extraer(texto):
    correos=re.findall(r"[\w.-]+@[\w.-]+\.\w+",texto)
    telefonos=re.findall(r"\+?\d[\d -]{7,}\d",texto)
    return {"correos":correos,"telefonos":telefonos}
print(extraer("Escribe a karen@ejemplo.com o llama al +58 412 555 0198"))
