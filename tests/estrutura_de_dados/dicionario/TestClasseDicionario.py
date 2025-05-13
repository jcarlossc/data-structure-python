import unittest
from estrutura_de_dados.dicionario.ClasseDicionario import ClasseDicionario
class TestClasseDicionario(unittest.TestCase):
    
    def setUp(self):
        self.dicionario = ClasseDicionario()

    def test_adicionar_e_listar(self):
        self.dicionario.adicionar('carlos', 47)
        self.dicionario.adicionar('maria', 2)
        resultado = {
            0: {'Nome': 'carlos', 'Idade': 47},
            1: {'Nome': 'maria', 'Idade': 2}
        }
        self.assertEqual(self.dicionario.listar(), resultado)

    def test_pesquisar(self):
        self.dicionario.adicionar('teresa', 44)
        self.dicionario.adicionar('jose', 45)
        resultado = self.dicionario.pesquisar(0)
        self.assertEqual(resultado, {'Nome': 'teresa', 'Idade': 44})

    def test_pesquisar_inexistente(self):
        resultado = self.dicionario.pesquisar(99)
        self.assertIsNone(resultado)

    def test_copiar(self):
        self.dicionario.adicionar("Carlos", 28)
        copia = self.dicionario.copiar()
        self.assertEqual(copia, self.dicionario.listar())
        self.assertIsNot(copia, self.dicionario.listar()) 

    def test_excluir(self):
        self.dicionario.adicionar("soares", 33)
        excluido = self.dicionario.excluir(0)
        self.assertEqual(excluido, {'Nome': 'soares', 'Idade': 33})
        self.assertEqual(self.dicionario.listar(), {})

    def test_limpar(self):
        self.dicionario.adicionar('maria', 22)
        self.dicionario.adicionar('costa', 31)
        self.dicionario.limpar()
        self.assertEqual(self.dicionario.listar(), {})