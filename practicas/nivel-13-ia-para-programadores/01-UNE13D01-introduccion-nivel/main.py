import json
plan={"nivel":13,"proyecto":"Aplicación con IA","herramientas":["Python","APIs de IA","GitHub Copilot","GitHub Actions"],"meta":"Construir, probar y desplegar una aplicación con IA integrada"}
print(json.dumps(plan,ensure_ascii=False,indent=2))
