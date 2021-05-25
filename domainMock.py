from unittest import mock
import unittest
from unittest.mock import patch,MagicMock
from domainInsercion import insertarDatos
from pokemon import pokebase
from entrenador import entrenadorbase


class testMockDomain(unittest.TestCase):
    
    
    
    @patch('domainInsercion.insertarDatos.insert_entrenador_data',return_value=True)
    def test_funcionaCorrecto(self,mock_get):
     llamar=insertarDatos()
     resultado_esperado=True
     resultado_actual=llamar.insert_entrenador_data("mock")
     
     assert resultado_esperado==resultado_actual
        
    @patch('domainInsercion.insertarDatos.eliminarEquipo',return_value="Se borraron los pokemon correctamente")
    def test_eliminar_equipo(self,mock_get):
     llamar=insertarDatos()
    
     resultado_esperado="Se borraron los pokemon correctamente"
     resultado_actual=llamar.eliminarEquipo("mock",1)
     
     assert resultado_esperado==resultado_actual
     
    @patch('domainInsercion.insertarDatos.eliminarEquipo',return_value="No se eliminó")
    def test_eliminar_equipo_dos(self,mock_get):
     llamar=insertarDatos()
    
     resultado_esperado="No se eliminó"
     resultado_actual=llamar.eliminarEquipo("mock",1)
     
     assert resultado_esperado==resultado_actual
    
    @patch('domainInsercion.insertarDatos.get_entrenador_data',return_value=1)
    def test_get_data_entrenador(self,mock_get):
     llamar=insertarDatos()
    
     resultado_esperado=1
     resultado_actual=llamar.get_entrenador_data("mock")
     
     assert resultado_esperado==resultado_actual


if __name__ == "__main__":
    unittest.main()