from datetime import datetime
from unittest.mock import Mock

import pytest
from notificaciones import enviar_recordatorio


def test_envio_con_fixture_y_mock(usuario_activo):
    cliente = Mock()
    cliente.enviar.return_value = {"enviado": True}
    resultado = enviar_recordatorio(usuario_activo, cliente, datetime(2027, 6, 9))
    assert resultado["enviado"] is True
    cliente.enviar.assert_called_once_with(
        "estudiante@example.com", "Recordatorio 2027-06-09"
    )


@pytest.mark.parametrize("activo", [False, None, 0])
def test_usuario_inactivo_no_envia(activo):
    cliente = Mock()
    resultado = enviar_recordatorio(
        {"correo": "a@example.com", "activo": activo}, cliente
    )
    assert resultado["motivo"] == "usuario inactivo"
    cliente.enviar.assert_not_called()
