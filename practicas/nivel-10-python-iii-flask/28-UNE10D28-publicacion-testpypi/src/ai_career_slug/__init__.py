import re
import unicodedata


__version__ = "0.1.0"


def crear_slug(texto):
    normalizado = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", normalizado).strip("-")


__all__ = ["crear_slug"]
