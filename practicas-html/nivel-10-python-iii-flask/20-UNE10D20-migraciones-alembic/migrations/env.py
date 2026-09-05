from logging.config import fileConfig

from alembic import context
from flask import current_app


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def obtener_motor():
    return current_app.extensions["migrate"].db.engine


def obtener_metadatos():
    return current_app.extensions["migrate"].db.metadata


def migraciones_sin_conexion():
    context.configure(url=str(obtener_motor().url), target_metadata=obtener_metadatos(), literal_binds=True, dialect_opts={"paramstyle": "named"}, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()


def migraciones_con_conexion():
    with obtener_motor().connect() as conexion:
        context.configure(connection=conexion, target_metadata=obtener_metadatos(), compare_type=True, render_as_batch=True)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    migraciones_sin_conexion()
else:
    migraciones_con_conexion()
