import unittest
from contraseña import validar_contraseña

class TestValidarContraseña(unittest.TestCase):

    def test_corta(self):
        self.assertEqual(validar_contraseña("hola"), "Contraseña demasiado corta")

    def test_sin_numero(self):
        self.assertEqual(validar_contraseña("Holamundo"), "Debe contener al menos un número")

    def test_sin_mayuscula(self):
        self.assertEqual(validar_contraseña("holamundo1"), "Debe contener al menos una mayúscula")

    def test_valida(self):
        self.assertEqual(validar_contraseña("Hola1234*"), "Contraseña válida")

    def test_exactamente_ocho(self):
        self.assertEqual(validar_contraseña("HOLA1234#"), "Contraseña válida")

    def test_solo_mayuscula_y_numero(self):
        self.assertEqual(validar_contraseña("HOLA123"), "Contraseña demasiado corta")

    def test_caracter_especial(self):
        self.assertEqual(validar_contraseña("HOLA123456"),"Debe contener al menos un carácter especial")
    def test_muy_larga(self):
        self.assertEqual(validar_contraseña("Hola1234*56789"),"Contraseña demasiado larga")
if __name__ == '__main__':
    unittest.main()
