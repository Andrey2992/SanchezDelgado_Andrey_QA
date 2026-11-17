def validar_password(password: str) -> bool:
    if password is None:
        return False
    
    if password == "":
        return False
    
    if len(password) < 8:
        return False
    
    if len(password) > 20:
        return False
    
    if not any(c.isupper() for c in password): #si no hay una mayúscula, devuelve False
        return False
    
    if not any(c.isdigit() for c in password):
        return False

    if " " in password:
        return False

    return True

def calcular_envio(subtotal: float) -> int:
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo")
    elif subtotal >= 25000:
        return 0
    else:
        return 2500
    
