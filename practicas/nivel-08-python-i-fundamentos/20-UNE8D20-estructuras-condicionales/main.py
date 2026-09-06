def calcular_envio(subtotal, distancia, cliente_premium=False):
    if subtotal < 0 or distancia < 0:
        raise ValueError("Los valores no pueden ser negativos")
    if cliente_premium or subtotal >= 1000:
        return 0.0
    if distancia <= 10:
        return 8.0
    if distancia <= 50:
        return 18.0
    return 35.0


def clasificar_ticket(impacto, urgencia, bloquea_operacion):
    if bloquea_operacion:
        return "crítica"
    if impacto == "alto" and urgencia == "alta":
        return "alta"
    if impacto == "bajo" and urgencia == "baja":
        return "baja"
    return "media"


def decidir_atencion(cliente, subtotal, distancia, impacto, urgencia, bloquea):
    prioridad = clasificar_ticket(impacto, urgencia, bloquea)
    envio = calcular_envio(subtotal, distancia, cliente["premium"])
    if prioridad in {"crítica", "alta"}:
        canal = "Atención inmediata"
    elif cliente["premium"]:
        canal = "Atención preferente"
    else:
        canal = "Cola general"
    return prioridad, envio, canal


def main():
    cliente = {"nombre": "Ana Torres", "premium": True}
    prioridad, envio, canal = decidir_atencion(
        cliente,
        subtotal=620,
        distancia=28,
        impacto="alto",
        urgencia="alta",
        bloquea=False,
    )
    print(f'Cliente: {cliente["nombre"]}')
    print(f"Prioridad: {prioridad}")
    print(f"Envío: {envio:.2f}")
    print(f"Canal: {canal}")


if __name__ == "__main__":
    main()
