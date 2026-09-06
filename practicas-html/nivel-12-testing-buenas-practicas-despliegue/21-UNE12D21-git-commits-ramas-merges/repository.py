import subprocess
from pathlib import Path


def ejecutar_git(ruta, *argumentos):
    resultado = subprocess.run(
        ["git", *argumentos],
        cwd=ruta,
        check=True,
        capture_output=True,
        text=True,
    )
    return resultado.stdout.strip()


def escribir(ruta, contenido):
    Path(ruta).write_text(contenido, encoding="utf-8")


def crear_flujo(ruta):
    ruta = Path(ruta)
    ruta.mkdir(parents=True, exist_ok=True)
    ejecutar_git(ruta, "init", "-b", "main")
    ejecutar_git(ruta, "config", "user.name", "AI Career")
    ejecutar_git(ruta, "config", "user.email", "student@example.com")
    escribir(ruta / "estado.txt", "versión inicial\n")
    ejecutar_git(ruta, "add", "estado.txt")
    ejecutar_git(ruta, "commit", "-m", "Crea versión inicial")
    ejecutar_git(ruta, "switch", "-c", "feature/estado")
    escribir(ruta / "estado.txt", "versión inicial\nestado validado\n")
    ejecutar_git(ruta, "add", "estado.txt")
    ejecutar_git(ruta, "commit", "-m", "Agrega estado validado")
    ejecutar_git(ruta, "switch", "main")
    ejecutar_git(ruta, "merge", "--no-ff", "feature/estado", "-m", "Integra estado")
    return {
        "rama": ejecutar_git(ruta, "branch", "--show-current"),
        "historial": ejecutar_git(ruta, "log", "--pretty=%s").splitlines(),
        "contenido": (ruta / "estado.txt").read_text(encoding="utf-8").splitlines(),
    }
