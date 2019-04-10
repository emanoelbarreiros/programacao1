import unittest
import regras

class TestRegras(unittest.TestCase):

    def test_jogada_valida(self):
        tabuleiro = [
            ['X', '_', '_'],
            ['_', 'O', '_'],
            ['X', '_', '_']]
        self.assertTrue(regras.jogada_valida(tabuleiro, 0, 1))
        self.assertFalse(regras.jogada_valida(tabuleiro, 0, 0))
        self.assertFalse(regras.jogada_valida(tabuleiro, -1, 0))
        self.assertFalse(regras.jogada_valida(tabuleiro, 0, -1))
        self.assertFalse(regras.jogada_valida(tabuleiro, 0, 4))
        self.assertFalse(regras.jogada_valida(tabuleiro, 4, 0))

    def test_intervalo_permitido(self):
        self.assertTrue(regras.intervalo_permitido(0,0))
        self.assertTrue(regras.intervalo_permitido(0,1))
        self.assertTrue(regras.intervalo_permitido(0,2))
        self.assertTrue(regras.intervalo_permitido(0,0))
        self.assertTrue(regras.intervalo_permitido(1,0))
        self.assertTrue(regras.intervalo_permitido(2,0))
        self.assertFalse(regras.intervalo_permitido(4,0))
        self.assertFalse(regras.intervalo_permitido(0,4))
    
    def test_ganhador(self):
        tabuleiro0 = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]
        tabuleiro1 = [
            ['X', 'X', 'X'],
            ['_', '_', '_'],
            ['_', '_', '_']]
        tabuleiro2 = [
            ['_', '_', '_'],
            ['X', 'X', 'X'],
            ['_', '_', '_']]
        tabuleiro3 = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['X', 'X', 'X']]
        tabuleiro4 = [
            ['X', '_', '_'],
            ['X', '_', '_'],
            ['X', '_', '_']]
        tabuleiro5 = [
            ['_', 'X', '_'],
            ['_', 'X', '_'],
            ['_', 'X', '_']]
        tabuleiro6 = [
            ['_', '_', 'X'],
            ['_', '_', 'X'],
            ['_', '_', 'X']]
        tabuleiro7 = [
            ['X', '_', '_'],
            ['_', 'X', '_'],
            ['_', '_', 'X']]
        tabuleiro8 = [
            ['_', '_', 'X'],
            ['_', 'X', '_'],
            ['X', '_', '_']]
        tabuleiro9 = [
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']]
        self.assertEqual(regras.ganhador(tabuleiro0), 'N')

        self.assertEqual(regras.ganhador(tabuleiro1), 'X')
        self.assertEqual(regras.ganhador(tabuleiro2), 'X')
        self.assertEqual(regras.ganhador(tabuleiro3), 'X')
        self.assertEqual(regras.ganhador(tabuleiro4), 'X')
        self.assertEqual(regras.ganhador(tabuleiro5), 'X')
        self.assertEqual(regras.ganhador(tabuleiro6), 'X')
        self.assertEqual(regras.ganhador(tabuleiro7), 'X')
        self.assertEqual(regras.ganhador(tabuleiro8), 'X')

        self.substituir(tabuleiro1, 'X', 'O')
        self.substituir(tabuleiro2, 'X', 'O')
        self.substituir(tabuleiro3, 'X', 'O')
        self.substituir(tabuleiro4, 'X', 'O')
        self.substituir(tabuleiro5, 'X', 'O')
        self.substituir(tabuleiro6, 'X', 'O')
        self.substituir(tabuleiro7, 'X', 'O')
        self.substituir(tabuleiro8, 'X', 'O')

        self.assertEqual(regras.ganhador(tabuleiro1), 'O')
        self.assertEqual(regras.ganhador(tabuleiro2), 'O')
        self.assertEqual(regras.ganhador(tabuleiro3), 'O')
        self.assertEqual(regras.ganhador(tabuleiro4), 'O')
        self.assertEqual(regras.ganhador(tabuleiro5), 'O')
        self.assertEqual(regras.ganhador(tabuleiro6), 'O')
        self.assertEqual(regras.ganhador(tabuleiro7), 'O')
        self.assertEqual(regras.ganhador(tabuleiro8), 'O')

        self.assertEqual(regras.ganhador(tabuleiro9), 'E')

    
    def substituir(self, lista, item_atual, item_substituir):
        for i_l, v_l in enumerate(lista):
            for i_c, v_c in enumerate(v_l):
                if v_c == item_atual:
                    lista[i_l][i_c] = item_substituir