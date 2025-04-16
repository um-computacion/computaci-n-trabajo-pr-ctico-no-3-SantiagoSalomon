import unittest
from unittest.mock import patch

class ValueError(Exception):
    pass

class NumeroDebeSerPositivo(Exception):
    pass

def ingrese_numero():
    try:
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")

class TestValidacionNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()
    
    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()
    
    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 0)
    
    @patch('builtins.input', return_value='3.14')
    def test_ingreso_decimal(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 3.14)

if __name__ == '__main__':
    unittest.main()