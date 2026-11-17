import pytest
from shopgo.validaciones import validar_password, calcular_envio

@pytest.mark.parametrize("password", ["Clave123", "ValidPass123", "Clave123456789012345", "NOLOWERCASE1"])
def test_validar_password(password):
    assert validar_password(password) is True 


@pytest.mark.parametrize("password", ["", None, "nouppercase1", "NoNumber", "Clave1234567890123456", "ClaveConEspacio 1", "Clave12"]) # "" vacio y none valor ausente
def test_invalidar_password(password):
    assert validar_password(password) is False


@pytest.mark.parametrize("subtotal, envio_esperado", [(0, 2500),(10000, 2500),(25000, 0),(30000, 0), (24999, 2500), (25001, 0)])
def test_calcular_envio(subtotal, envio_esperado):
    assert calcular_envio(subtotal) == envio_esperado

@pytest.mark.parametrize("subtotal", [-1, -100, -0.01])
def test_calcular_envio_negativo(subtotal):
    with pytest.raises(ValueError):
            calcular_envio(subtotal)