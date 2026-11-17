from pages.login_page import LoginPage

def test_login_muestra_bienvenida(driver):
    pagina = LoginPage(driver)
    pagina.ingresar_email("usuario@ejemplo.com")
    pagina.ingresar_contraseña("Clave123")
    pagina.pulsar_login()
    assert pagina.obtener_titulo_principal() == "Bienvenido"


def test_login_muestra_error(driver):
    pagina = LoginPage(driver)
    pagina.ingresar_email("usuario@ejemplo.com")
    pagina.ingresar_contraseña("ClaveIncorrecta123")
    pagina.pulsar_login()
    assert pagina.obtener_error() == "Correo o contraseña incorrectos"