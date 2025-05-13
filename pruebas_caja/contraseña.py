
def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "Contraseña demasiado corta"
    if not any(c.isdigit() for c in contraseña):
        return "Debe contener al menos un número"
    if not any(c.isupper() for c in contraseña):
        return "Debe contener al menos una mayúscula"
    if not any(c in "!#$%&*" for c in contraseña):
        return "Debe contener al menos un carácter especial"
    if len(contraseña) > 12:
        return "Contraseña demasiado larga"
    return "Contraseña válida"
