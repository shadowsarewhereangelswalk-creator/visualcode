import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Cliente:
    id: int | None
    nombre: str
    correo: str
    telefono: str
    servicio: str
    activo: bool = True

    @classmethod
    def crear(cls, nombre, correo, telefono, servicio, identificador=None, activo=True):
        nombre = " ".join(nombre.split()).title()
        correo = correo.strip().lower()
        telefono = telefono.strip()
        servicio = servicio.strip().title()
        if len(nombre) < 3:
            raise ValueError("Escribe un nombre válido")
        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
            raise ValueError("Escribe un correo válido")
        if not 10 <= len(re.sub(r"\D", "", telefono)) <= 15:
            raise ValueError("Escribe un teléfono válido")
        if len(servicio) < 3:
            raise ValueError("Escribe un servicio válido")
        return cls(identificador, nombre, correo, telefono, servicio, bool(activo))
