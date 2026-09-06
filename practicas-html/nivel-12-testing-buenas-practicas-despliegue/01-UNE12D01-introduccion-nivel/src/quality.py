def evaluar_pipeline(resultados):
    etapas = ("tests", "lint", "format", "coverage", "build")
    faltantes = [etapa for etapa in etapas if not resultados.get(etapa, False)]
    return {
        "etapas": len(etapas),
        "aprobadas": len(etapas) - len(faltantes),
        "faltantes": faltantes,
        "listo_para_desplegar": not faltantes,
    }
