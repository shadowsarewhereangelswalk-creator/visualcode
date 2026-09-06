from datetime import datetime


class ClienteCorreo:
    def enviar(self, destinatario, asunto):
        return {"destinatario": destinatario, "asunto": asunto, "enviado": True}


def enviar_recordatorio(usuario, cliente, ahora=None):
    ahora = ahora or datetime.now()
    if not usuario.get("activo", False):
        return {"enviado": False, "motivo": "usuario inactivo"}
    asunto = f"Recordatorio {ahora:%Y-%m-%d}"
    return cliente.enviar(usuario["correo"], asunto)
