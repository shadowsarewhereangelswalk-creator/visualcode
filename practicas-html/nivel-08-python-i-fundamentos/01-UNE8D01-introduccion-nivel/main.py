from datetime import date

nivel = {
    "nombre": "Nivel 8 — Python I: Fundamentos",
    "proyecto": "Aplicación de consola",
    "duracion": 28,
    "inicio": date(2027, 2, 1),
    "herramientas": ("Python", "Visual Studio Code", "Terminal"),
}

practicas = [
    {"codigo": "P1", "dia": 8, "entrega": "Gestor de colecciones"},
    {"codigo": "P2", "dia": 15, "entrega": "Script de decisiones y ciclos"},
    {"codigo": "P3", "dia": 19, "entrega": "Biblioteca de funciones"},
    {"codigo": "P4", "dia": 23, "entrega": "Programa orientado a objetos"},
    {"codigo": "P5", "dia": 27, "entrega": "Aplicación con archivos"},
]


def mostrar_plan(datos, entregas):
    print(datos["nombre"])
    print(f'Proyecto: {datos["proyecto"]}')
    print(f'Duración: {datos["duracion"]} clases')
    print(f'Inicio: {datos["inicio"].strftime("%d/%m/%Y")}')
    print("Herramientas:", ", ".join(datos["herramientas"]))
    print("Entregas:")
    for practica in entregas:
        print(f'  {practica["codigo"]} · día {practica["dia"]}: {practica["entrega"]}')


if __name__ == "__main__":
    mostrar_plan(nivel, practicas)
