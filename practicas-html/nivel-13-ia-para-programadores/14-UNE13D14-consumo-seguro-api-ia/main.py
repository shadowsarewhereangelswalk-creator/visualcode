import os
from urllib.parse import urlparse
def validar(url,clave):
    if urlparse(url).scheme!="https": raise ValueError("La API debe usar HTTPS")
    if len(clave)<12: raise ValueError("La clave debe almacenarse de forma segura")
    return True
print(validar(os.getenv("AI_API_URL","https://api.example.com/v1"),os.getenv("AI_API_KEY","clave-segura-demo")))
