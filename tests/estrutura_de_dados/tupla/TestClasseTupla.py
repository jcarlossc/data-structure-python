import unittest

from estrutura_de_dados.tupla.ClasseTupla import ClasseTupla

class TestClasseTupla(unittest.TestCase):
    """Classe de testes para a classe ClasseTupla."""

    def setUp(self):
        """Configuração do objeto tupla."""
        self.tupla = ClasseTupla()

    def test_listar(self):
        """Teste para validar o método listar."""
        self.tupla.adicionar('carlos')
        self.assertEqual(self.tupla.listar(), ('carlos',))      
        self.assertNotEqual(self.tupla.listar(), ('jose',)) 

    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.tupla.adicionar('soares')
        self.assertEqual(self.tupla.listar(), ('soares',))      
        self.assertNotEqual(self.tupla.listar(), ('jose',)) 

    def test_contar_ocorrencias(self):
        """Teste para validar o método contar_ocorrencias."""
        self.tupla.adicionar('soares')
        self.tupla.adicionar('teresa')
        self.tupla.adicionar('teresa')
        self.assertEqual(self.tupla.contar_ocorrencias('teresa'), 2)      
        self.assertNotEqual(self.tupla.contar_ocorrencias('teresa'), 1)     

    def test_buscar_indice(self):
        """Teste para validar o método buscar_indice."""
        self.tupla.adicionar('soares')
        self.tupla.adicionar('teresa')
        self.tupla.adicionar('soares')
        self.assertEqual(self.tupla.buscar_indice('teresa'), 1)      
        self.assertNotEqual(self.tupla.buscar_indice('teresa'), 2)     

    def test_quantidade(self):
        """Teste para validar o método quantidade."""
        self.tupla.adicionar('carlos')
        self.tupla.adicionar('teresa')
        self.tupla.adicionar('soares')
        self.assertEqual(self.tupla.quantidade(), 3)      
        self.assertNotEqual(self.tupla.quantidade(), 2)       

    def test_ordem_maxima(self):
        """Teste para validar o método ordem_maxima."""
        self.tupla.adicionar('carlos')
        self.tupla.adicionar('teresa')
        self.tupla.adicionar('soares')
        self.assertEqual(self.tupla.ordem_maxima(), 'teresa')      
        self.assertNotEqual(self.tupla.ordem_maxima(), 'soares')          

    def test_ordem_minima(self):
        """Teste para validar o método ordem_minima."""
        self.tupla.adicionar('carlos')
        self.tupla.adicionar('teresa')
        self.tupla.adicionar('soares')
        self.assertEqual(self.tupla.ordem_minima(), 'carlos')      
        self.assertNotEqual(self.tupla.ordem_minima(), 'teresa')          