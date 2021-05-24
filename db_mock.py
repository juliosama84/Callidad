from PokeApi import PokeApi
from unittest import TestCase
from unittest.mock import patch, Mock
from baseConection import DataBaseInteract
from entrenador import entrenadorbase
import unittest

class TestOperaciones(unittest.TestCase):
    @patch("baseConection.DataBaseInteract.insert_user",return_value=True)
    def test_insert_Usuario(self,mock_get):
        llamar=DataBaseInteract()
        
        esperado=True
        resultado_actual=llamar.insert_user("mock")
        assert esperado==resultado_actual
        
    @patch("baseConection.DataBaseInteract.inserta_poke",return_value=True)
    def test_insert_poke(self,mock_get):
        llamar=DataBaseInteract()
        
        esperado=True
        resultado_actual=llamar.inserta_poke("mock")
        assert esperado==resultado_actual
        
    @patch("baseConection.DataBaseInteract.delete_poke",return_value="Se borraron los pokemon correctamente")
    def test_delete_poke(self,mock_get):
        llamar=DataBaseInteract()
        
        esperado="Se borraron los pokemon correctamente"
        resultado_actual=llamar.delete_poke("mock")
        assert esperado==resultado_actual


if __name__ == "__main__":
    unittest.main()