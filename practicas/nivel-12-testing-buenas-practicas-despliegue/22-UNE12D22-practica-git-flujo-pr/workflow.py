import subprocess
import sys
from pathlib import Path


def ejecutar(ruta, *argumentos):
    resultado = subprocess.run(
        ["git", *argumentos],
        cwd=ruta,
        check=True,
        capture_output=True,
        text=True,
    )
    return resultado.stdout.strip()


def preparar_repositorio(ruta):
    ruta = Path(ruta)
    ruta.mkdir(parents=True, exist_ok=True)
    ejecutar(ruta, "init", "-b", "main")
    ejecutar(ruta, "config", "user.name", "AI Career")
    ejecutar(ruta, "config", "user.email", "student@example.com")
    (ruta / "status.py").write_text(
        'def obtener_estado():\n    return {"servicio": "activo"}\n',
        encoding="utf-8",
    )
    ejecutar(ruta, "add", "status.py")
    ejecutar(ruta, "commit", "-m", "Crea servicio de estado")
    ejecutar(ruta, "switch", "-c", "feature/pruebas-estado")
    prueba = (
        "from status import obtener_estado\n\n\n"
        "def test_estado():\n"
        '    assert obtener_estado()["servicio"] == "activo"\n'
    )
    (ruta / "test_status.py").write_text(
        prueba,
        encoding="utf-8",
    )
    ejecutar(ruta, "add", "test_status.py")
    ejecutar(ruta, "commit", "-m", "Agrega pruebas del servicio")
    return ruta


def revisar_cambios(ruta):
    return {
        "archivos": ejecutar(ruta, "diff", "--name-only", "main...HEAD").splitlines(),
        "commits": ejecutar(ruta, "log", "--pretty=%s", "main..HEAD").splitlines(),
    }


def aprobar_y_fusionar(ruta):
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=ruta,
        check=True,
        capture_output=True,
        text=True,
    )
    ejecutar(ruta, "switch", "main")
    ejecutar(
        ruta,
        "merge",
        "--no-ff",
        "feature/pruebas-estado",
        "-m",
        "Integra pruebas de estado",
    )
    return ejecutar(ruta, "log", "-1", "--pretty=%s")
