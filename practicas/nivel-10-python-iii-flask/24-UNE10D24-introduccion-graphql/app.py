import sys


CURSOS = (
    {"id": "1", "nombre": "Python", "nivel": "inicial", "cupos": 20},
    {"id": "2", "nombre": "Flask", "nivel": "intermedio", "cupos": 15},
    {"id": "3", "nombre": "APIs", "nivel": "intermedio", "cupos": 18},
)
INSCRIPCIONES = []


def buscar_curso(curso_id):
    return next((curso for curso in CURSOS if curso["id"] == str(curso_id)), None)


if "--check" in sys.argv:
    assert buscar_curso(2)["nombre"] == "Flask"
    assert buscar_curso(99) is None
    print("UNE10D24 OK")
    raise SystemExit(0)


from flask import Flask, request
from graphql import GraphQLError, build_schema, graphql_sync


ESQUEMA = """
type Curso {
    id: ID!
    nombre: String!
    nivel: String!
    cupos: Int!
}

type Inscripcion {
    id: ID!
    curso: Curso!
    nombre: String!
    correo: String!
}

type Query {
    cursos(nivel: String): [Curso!]!
    curso(id: ID!): Curso
}

type Mutation {
    inscribir(cursoId: ID!, nombre: String!, correo: String!): Inscripcion!
}
"""


schema = build_schema(ESQUEMA)


def resolver_cursos(objeto, info, nivel=None):
    return [curso for curso in CURSOS if nivel is None or curso["nivel"] == nivel.lower()]


def resolver_curso(objeto, info, id):
    return buscar_curso(id)


def resolver_inscribir(objeto, info, cursoId, nombre, correo):
    curso = buscar_curso(cursoId)
    if curso is None:
        raise GraphQLError("El curso no existe")
    if len(nombre.strip()) < 2 or "@" not in correo:
        raise GraphQLError("Nombre o correo no válido")
    inscripcion = {"id": str(len(INSCRIPCIONES) + 1), "curso": curso, "nombre": nombre.strip(), "correo": correo.strip().lower()}
    INSCRIPCIONES.append(inscripcion)
    return inscripcion


schema.get_type("Query").fields["cursos"].resolve = resolver_cursos
schema.get_type("Query").fields["curso"].resolve = resolver_curso
schema.get_type("Mutation").fields["inscribir"].resolve = resolver_inscribir


app = Flask(__name__)


@app.get("/")
def inicio():
    return {
        "servicio": "Academia GraphQL",
        "endpoint": "/graphql",
        "ejemplo": "{ cursos(nivel: \"intermedio\") { id nombre cupos } }",
    }


@app.post("/graphql")
def graphql():
    datos = request.get_json(silent=True) or {}
    consulta = datos.get("query")
    if not isinstance(consulta, str) or not consulta.strip():
        return {"errors": [{"message": "La consulta GraphQL es obligatoria"}]}, 400
    resultado = graphql_sync(schema, consulta, variable_values=datos.get("variables"), operation_name=datos.get("operationName"))
    respuesta = {}
    if resultado.data is not None:
        respuesta["data"] = resultado.data
    if resultado.errors:
        respuesta["errors"] = [{"message": error.message} for error in resultado.errors]
    return respuesta, 400 if resultado.errors and resultado.data is None else 200


if __name__ == "__main__":
    app.run()
