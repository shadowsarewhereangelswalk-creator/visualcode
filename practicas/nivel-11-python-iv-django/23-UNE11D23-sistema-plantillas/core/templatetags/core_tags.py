from django import template


register = template.Library()


@register.filter
def estado_texto(valor):
    return {"nuevo": "Nuevo", "activo": "En curso", "listo": "Finalizado"}.get(valor, valor)


@register.inclusion_tag("core/componentes/indicador.html")
def indicador(etiqueta, valor):
    return {"etiqueta": etiqueta, "valor": valor}

