from pathlib import Path
Path("Procfile").write_text("web: python app.py\n",encoding="utf-8")
Path("runtime.txt").write_text("python-3.12\n",encoding="utf-8")
Path("requirements.txt").write_text("\n",encoding="utf-8")
print("Archivos de despliegue creados")
